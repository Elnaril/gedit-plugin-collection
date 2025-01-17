from gi.repository import GObject, Gedit, Gio


class JsonFormatterAppActivatable(GObject.Object, Gedit.AppActivatable):
    app = GObject.property(type=Gedit.App)
    __gtype_name__ = "JsonFormatterAppActivatable"

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self._build_menu()

    def do_deactivate(self):
        self._remove_menu()

    def _build_menu(self):
        self.menu_ext = self.extend_menu("tools-section")
        menu = Gio.Menu()
        sub_menu = Gio.MenuItem.new_submenu("JSON", menu)
        sub_menu_item_verify = Gio.MenuItem.new("Verify", 'win.verify_json')
        menu.append_item(sub_menu_item_verify)
        sub_menu_item_format = Gio.MenuItem.new("Format", 'win.format_json')
        menu.append_item(sub_menu_item_format)
        sub_menu_item_minimify = Gio.MenuItem.new("Minimify", 'win.minimify_json')
        menu.append_item(sub_menu_item_minimify)
        self.menu_ext.append_menu_item(sub_menu)

        self.app.set_accels_for_action("win.verify_json", ("<Primary><Alt>v", None))
        self.app.set_accels_for_action("win.format_json", ("<Primary><Alt><Shift>j", None))
        self.app.set_accels_for_action("win.minimify_json", ("<Primary><Alt>j", None))


    def _remove_menu(self):
        self.menu_ext = None
