import tkinter
import customtkinter
import json, yaml
from modules.settings_frame import SettingsFrame
from modules.status_frame import StatusFrame

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.test = "test"

        self.read_settings()
        self.read_string_table()        

        self.title(self.text['title'])
        self.geometry("640x480")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.settings_frame = SettingsFrame(self)
        self.settings_frame.grid(row=0, column=0, padx=(10,5), pady=10, sticky="nsew")
        self.status_frame = StatusFrame(self)
        self.status_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(0,10), sticky="sew")
        

    def read_settings(self):
        with open('config/settings.json', 'r', encoding='utf-8') as settings_file:
            self.settings = json.load(settings_file)

    def save_settings(self):
        with open('config/settings.json', 'w', encoding='utf-8') as settings_file:
            json.dump(self.settings, settings_file, indent=4, ensure_ascii=False)
    
    def read_string_table(self):
        with open(f"lang/{self.settings['language']}.yaml", 'r', encoding='utf-8') as text_file:
            self.text = yaml.safe_load(text_file)
        


app = App()
app.mainloop()