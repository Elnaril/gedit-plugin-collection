import json

from gi.repository import GObject, Gedit, Gio


atomic_delimiters = {
    "<": ">",
    "'": "'",
    '"': '"',
    "#": "\n",
}


breakers = [
    ",",
    ";",
]

composite_delimiters = {
    "[": "]",
    "{": "}",
    "(": ")",
}


class PrettifierWindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "PrettifierWindowActivatable"
    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        action_prettify = Gio.SimpleAction.new("prettify", None)
        action_prettify.connect("activate", self.on_prettify)
        self.window.add_action(action_prettify)

        self.statusbar = self.window.get_statusbar()
        self.statusbar_context_id = self.statusbar.get_context_id("Prettifier")

    def do_deactivate(self):
        self.statusbar.remove_all(self.statusbar_context_id)

    def do_update_state(self):
        self.statusbar.remove_all(self.statusbar_context_id)

    def get_current_text(self) -> str:
        doc = self.window.get_active_document()
        if not doc:
            return ""
        return doc.get_text(
            start=doc.get_start_iter(),
            end=doc.get_end_iter(),
            include_hidden_chars=False,
        )

    def set_new_text(self, text: str) -> None:
        doc = self.window.get_active_document()
        if not doc:
            return
        doc.set_text(text)

    def on_prettify(self, action, data):
        text = self.get_current_text()
        try:
            self.set_new_text(self.prettify(text))
        except ValueError as e:
            self.statusbar.push(self.statusbar_context_id, f"⚠️ {e}")


    def _new_line(self, offset) -> list:
        new_line = ["\n"]
        new_line.extend([" "] * offset)
        return new_line

    def prettify(self, text: str) -> str:
        result = []
        inside_atomic = False
        atomic_end = None
        offset = 0
        composite_stack = []
        for i, c in enumerate(text):
            # inside atomic: reach ends of do nothing
            if inside_atomic:
                if c == atomic_end:
                    inside_atomic = False
                    atomic_end = None
                    if i < len(text) - 2 and text[i + 1] not in breakers and text[i + 1] != ":" and text[i+1] not in composite_delimiters.values():
                        result.append(c)
                        result.extend(self._new_line(offset))
                        continue
                result.append(c)
                continue

            # start new atomic
            if c in atomic_delimiters.keys():
                inside_atomic = True
                atomic_end = atomic_delimiters.get(c)
                result.append(c)
                continue

            # one & one space only after colon
            if c == ":":
                result.append(":")
                result.append(" ")
                continue

            # No more than 1 space in a row, no line starting with a space
            if c == " " and len(result) > 0 and (result[-1] == " " or result[-1] == "\n"):
                continue

            # remove existing new lines
            if c == "\n":
                continue

            # New line after breaker
            if c in breakers:
                result.append(c)
                result.extend(self._new_line(offset))
                continue

            # start new composite
            if c in composite_delimiters.keys():
                composite_stack.append(composite_delimiters.get(c))
                result.append(c)
                offset += 4
                result.extend(self._new_line(offset))
                continue

            # end composite or raise error
            if c in composite_delimiters.values():
                if len(composite_stack) > 0 and composite_stack.pop(-1) == c:
                    offset -= 4
                    result.extend(self._new_line(offset))
                    result.append(c)
                    continue
                else:
                    raise ValueError(f"Unexpected {c}")
            result.append(c)
        return "".join(result)
