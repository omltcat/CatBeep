import customtkinter
from modules.indicator_bar import GIndicator, AOAIndicator

class IndicatorsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.app = self.master

        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        # Indicators
        self.g_indicator = GIndicator(self, 'g_load', 0, (20,10))
        self.aoa_indicator = AOAIndicator(self, 'aoa', 1, (10,20))

