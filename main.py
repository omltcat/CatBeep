import customtkinter
import threading
import json, yaml
from modules.settings_frame import SettingsFrame
from modules.indicators_frame import IndicatorsFrame
from modules.status_frame import StatusFrame
from modules.udp_server import server

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.read_settings()
        self.read_string_table()

        self.font = customtkinter.CTkFont(self.strings['font'], 14)
        self.title(self.strings['title'])
        self.geometry("660x420")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1), weight=0)

        self.vars = {
            'status': 'not_running',
            'g': int(self.settings['over_g']['slider']/3),
            'aoa': int(self.settings['high_aoa']['slider']*2/3)
        }
        
        self.status_frame = StatusFrame(self)
        self.status_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(0,10), sticky="sew")
        self.settings_frame = SettingsFrame(self)
        self.settings_frame.grid(row=0, column=0, padx=(10,5), pady=10, sticky="nsew")
        self.indicators_frame = IndicatorsFrame(self)
        self.indicators_frame.grid(row=0, column=1, padx=(5,10), pady=10, sticky="nsew")
        

    def read_settings(self):
        with open('config/settings.json', 'r', encoding='utf-8') as settings_file:
            self.settings = json.load(settings_file)

    def save_settings(self):
        with open('config/settings.json', 'w', encoding='utf-8') as settings_file:
            json.dump(self.settings, settings_file, indent=4, ensure_ascii=False)
    
    def read_string_table(self):
        with open(f"lang/{self.settings['language']}.yaml", 'r', encoding='utf-8') as strings_file:
            self.strings = yaml.safe_load(strings_file)

    def set_var(self, var, value):
        self.vars[var] = value

    def get_var(self, var):
        return self.vars[var]

    def get_setting(self, level_1, level_2=None):
        return self.settings[level_1] if level_2 is None else self.settings[level_1][level_2]
    
    def set_setting(self, value, level_1, level_2=None):
        if level_2 is None:
            self.settings[level_1] = value
        else:
            self.settings[level_1][level_2] = value

    def get_string(self, level_1, level_2=None):
        return self.strings[level_1] if level_2 is None else self.strings[level_1][level_2]


app = App()
threading.Thread(target=lambda: server(app=app), daemon=True).start()
app.mainloop()