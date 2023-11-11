import customtkinter
from modules.checkbox_slider import CheckBoxSlider
from modules.dropdown_menu import LanguageMenu, AudioOutputMenu
from modules.volume_slider import GVolumeSlider, AoAVolumeSlider

class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.app = self.master

        self.grid_columnconfigure((0,1), weight=1)

        self.lang_menu = LanguageMenu(self, "language", row=0, pady=(15,0))
        self.audio_output = AudioOutputMenu(self, "audio_output", row=1, pady=(15,0))
        self.med_g = CheckBoxSlider(self, "med_g", row=2, blockers=(None, "high_g"))
        self.high_g = CheckBoxSlider(self, "high_g", row=3, blockers=("med_g", "over_g"))
        self.over_g = CheckBoxSlider(self, "over_g", row=4, blockers=("high_g", None))
        self.high_aoa = CheckBoxSlider(self, "high_aoa", row=5, limits=(0,300), unit="°")
        self.g_volume = GVolumeSlider(self, "g_volume", row=6, pady=(17,0))
        self.aoa_volume = AoAVolumeSlider(self, "aoa_volume", row=7, pady=(15,20))
