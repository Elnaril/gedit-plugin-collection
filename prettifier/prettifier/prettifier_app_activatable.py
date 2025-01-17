from gi.repository import GObject, Gedit, Gio


class PrettifierAppActivatable(GObject.Object, Gedit.AppActivatable):
    app = GObject.property(type=Gedit.App)
    __gtype_name__ = "PrettifierAppActivatable"

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self._build_menu()

    def do_deactivate(self):
        self._remove_menu()

    def _build_menu(self):
        self.menu_ext = self.extend_menu("tools-section")
        menu_item_prettify = Gio.MenuItem.new("Prettify", 'win.prettify')
        self.menu_ext.append_menu_item(menu_item_prettify)
        self.app.set_accels_for_action("win.prettify", ("<Primary><Shift>p", None))


    def _remove_menu(self):
        self.menu_ext = None
