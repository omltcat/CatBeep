import customtkinter
import sounddevice as sd

class DropdownMenu():
    def __init__(self, master, name, row, pady=(10,0)):
        self.master = master
        self.app = master.app
        self.name = name
        self.row = row
        self.pady = pady
       
        self.label = customtkinter.CTkLabel(self.master, text=self.app.get_string('label', self.name), fg_color="transparent", font=self.app.font)
        self.menu = customtkinter.CTkOptionMenu(self.master, values=[""], command=self.menu_event, font=self.app.font, dynamic_resizing=False)

        self.label.grid(row=self.row, column=0, padx=(49,0), pady=self.pady, sticky="w")
        self.menu.grid(row=self.row, column=1, padx=(5,25), pady=self.pady, sticky="ew")

    # Function called upon selection, change this
    def menu_event(self, value):
        pass
        # print(f"{self.label.cget('text')}: {value}")

class LanguageMenu(DropdownMenu):
    def __init__(self, master, name, row, pady=...):
        super().__init__(master, name, row, pady)

        self.menu.configure(values=[self.app.get_string('menu','chinese'), self.app.get_string('menu','english')])
        self.menu.set(self.app.get_string('current_lang'))  # set initial value

    def menu_event(self, value):
        if value in ['中文', 'cn']:
            self.app.set_setting('cn', 'language')
        else:
            self.app.set_setting('en', 'language')
        self.app.read_string_table()
        self.app.save_settings()
        self.app.set_var('status', 'lang_restart')
        self.app.status_frame.update_text()

class AudioOutputMenu(DropdownMenu):
    def __init__(self, master, name, row, pady=...):
        super().__init__(master, name, row, pady)

        apis = sd.query_hostapis()
        ds = [i for i in apis if 'MME' in i['name']]

        if len(ds) == 0:
            self.menu.set(self.app.get_string('menu','no_audio_device'))
            self.app.set_var('status', 'no_audio_device')
            self.app.status_frame.update_text()
        else:
            self.default_device = ds[0]['default_output_device']
            self.devices = {i: sd.query_devices(i)['name'] for i in ds[0]['devices'] if sd.query_devices(i)['max_output_channels'] > 0}
            self.menu.configure(values=self.devices.values())
            saved_id = self.app.get_setting('audio_device', 'id')
            saved_name = self.app.get_setting('audio_device', 'name')
            if saved_id in self.devices and saved_name == self.devices[saved_id]:
                self.menu.set(saved_name)
            else:
                self.menu.set(self.devices[self.default_device])
                self.app.set_setting(self.default_device, 'audio_device', 'id')
                self.app.set_setting(self.devices[self.default_device], 'audio_device', 'name')

    def menu_event(self, value):
        device_id = list(self.devices.keys())[list(self.devices.values()).index(value)]
        self.app.set_setting(value, 'audio_device', 'name')
        self.app.set_setting(device_id, 'audio_device', 'id')
        self.app.save_settings()  
        self.app.restart_audio_threads()
        