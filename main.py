import customtkinter
import threading
import json, yaml
from modules.settings_frame import SettingsFrame
from modules.indicators_frame import IndicatorsFrame
from modules.status_frame import StatusFrame
from modules.udp_server import server
from modules.audio_stream import g_audio_stream, aoa_audio_stream
from modules.watchdog import watchdog

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.read_settings()
        self.read_string_table()

        self.font = customtkinter.CTkFont(self.strings['font'], 14)
        self.title(self.strings['title'])
        self.geometry("700x420")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1), weight=0)

        self.vars = {
            'status': 'idle',
            'g': int(self.settings['over_g']['slider']/10),
            'aoa': int(self.settings['high_aoa']['slider']*2/10),
            'audio_threads_on': False,
            'audio_can_play': False,
            'audio_testing': False,
            'last_received': -1
        }
        
        self.status_frame = StatusFrame(self)
        self.status_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(0,10), sticky="sew")
        self.settings_frame = SettingsFrame(self)
        self.settings_frame.grid(row=0, column=0, padx=(10,5), pady=10, sticky="nsew")
        self.indicators_frame = IndicatorsFrame(self)
        self.indicators_frame.grid(row=0, column=1, padx=(5,10), pady=10, sticky="nsew")
        
        self.start_audio_threads()
        self.server_thread = threading.Thread(target=lambda: server(app=self), daemon=True).start()
        self.watchdog_thread = threading.Thread(target=lambda: watchdog(app=self), daemon=True).start()

    def start_audio_threads(self):
        self.vars['audio_threads_on'] = True
        self.g_thread = threading.Thread(target=lambda: g_audio_stream(app=self), daemon=True).start()
        self.aoa_thread = threading.Thread(target=lambda: aoa_audio_stream(app=self), daemon=True).start()
        
    def restart_audio_threads(self):
        if self.vars['audio_threads_on']:
            self.vars['audio_threads_on'] = False
            self.after(500, lambda: self.start_audio_threads())
        else:
            self.start_audio_threads()

    def read_settings(self):
        try:
            with open('config/settings.json', 'r', encoding='utf-8') as settings_file:
                self.settings = json.load(settings_file)
        except FileNotFoundError:
            with open('config/settings_default.json', 'r', encoding='utf-8') as settings_file:
                self.settings = json.load(settings_file)
                self.save_settings()

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
app.mainloop()