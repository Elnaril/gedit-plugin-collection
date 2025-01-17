from gi.repository import GObject, Gedit

class JsonFormatterViewActivatable(GObject.Object, Gedit.ViewActivatable):
    __gtype_name__ = "JsonFormatterViewActivatable"
    view = GObject.property(type=Gedit.View)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        pass

    def do_deactivate(self):
        pass

    def do_update_state(self):
        pass
