import customtkinter
from modules.checkbox_slider import CheckBoxSlider
from modules.dropdown_menu import LanguageMenu

class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.app = self.master

        self.grid_columnconfigure((0,1), weight=1)

        self.lang_menu = LanguageMenu(self, "language", row=0, pady=(10,5))
        self.med_g = CheckBoxSlider(self, "med_g", row=1, blockers=(None, "high_g"))
        self.high_g = CheckBoxSlider(self, "high_g", row=2, blockers=("med_g", "over_g"))
        self.over_g = CheckBoxSlider(self, "over_g", row=3, blockers=("high_g", None))
        self.high_aoa = CheckBoxSlider(self, "high_aoa", row=4, limits=(0,300), unit="°")
        
    def get(self):
        checked_checkboxes = []
        if self.checkbox_1.get() == 1:
            checked_checkboxes.append(self.checkbox_1.cget("text"))
        if self.checkbox_2.get() == 1:
            checked_checkboxes.append(self.checkbox_2.cget("text"))
        if self.checkbox_3.get() == 1:
            checked_checkboxes.append(self.checkbox_3.cget("text"))
        return checked_checkboxes