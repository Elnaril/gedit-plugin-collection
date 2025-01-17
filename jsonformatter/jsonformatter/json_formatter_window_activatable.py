import json

from gi.repository import GObject, Gedit, Gio


class JsonFormatterWindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "JsonFormatterWindowActivatable"
    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        action_verify = Gio.SimpleAction.new("verify_json", None)
        action_verify.connect("activate", self.on_verify)
        self.window.add_action(action_verify)

        action_format = Gio.SimpleAction.new("format_json", None)
        action_format.connect("activate", self.on_format)
        self.window.add_action(action_format)

        action_minimify = Gio.SimpleAction.new("minimify_json", None)
        action_minimify.connect("activate", self.on_minimify)
        self.window.add_action(action_minimify)

        self.statusbar = self.window.get_statusbar()
        self.statusbar_context_id = self.statusbar.get_context_id("JSON Verify Result")

    def do_deactivate(self):
        self.statusbar.remove_all(self.statusbar_context_id)

    def do_update_state(self):
        self.statusbar.remove_all(self.statusbar_context_id)

    def is_valid_json(self, text: str) -> bool:
        try:
            _ = json.loads(text)
            return True
        except json.decoder.JSONDecodeError:
            return False

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

    def on_verify(self, action, data):
        if self.is_valid_json(self.get_current_text()):
            self.statusbar.push(self.statusbar_context_id, "✅ Valid JSON format")
        else:
            self.statusbar.push(self.statusbar_context_id, "⚠️ Invalid JSON format!")

    def on_format(self, action, data):
        try:
            json_doc = json.loads(self.get_current_text())
            self.set_new_text(json.dumps(json_doc, indent=4))
        except json.decoder.JSONDecodeError:
            self.statusbar.push(self.statusbar_context_id, "⚠️ Invalid JSON format!")

    def on_minimify(self, action, data):
        try:
            json_doc = json.loads(self.get_current_text())
            self.set_new_text(json.dumps(json_doc))
        except json.decoder.JSONDecodeError:
            self.statusbar.push(self.statusbar_context_id, "⚠️ Invalid JSON format!")
