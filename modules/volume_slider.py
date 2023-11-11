import customtkinter

class VolumeSlider():
    def __init__(self, master, name, row, pady=(15,0)):
        self.master = master
        self.app = master.app
        self.name = name
        self.row = row
        self.pady = pady

        self.label = customtkinter.CTkLabel(self.master, text=self.app.get_string('label', self.name), fg_color="transparent", font=self.app.font)
        self.button = customtkinter.CTkButton(self.master, text="▶", command=self.button_event, width=14, height=24)
        self.slider_value = customtkinter.IntVar(value=self.app.get_setting(self.name))
        self.slider = customtkinter.CTkSlider(self.master, from_=0, to=100, number_of_steps=100, variable=self.slider_value, width=10, command=self.slide_event)

        self.label.grid(row=self.row, column=0, padx=(49,0), pady=self.pady, sticky="w")
        self.slider.grid(row=self.row, column=1, padx=(0,20), pady=self.pady, sticky="ew")
        self.button.place(in_=self.slider, anchor="c", relx=-0.1, rely=0.5)

    def slide_event(self, value: int):
        self.app.set_setting(int(value), self.name)

    def button_event(self):
        pass

class GVolumeSlider(VolumeSlider):
    def button_event(self):
        self.app.set_var('audio_testing', True)
        self.app.set_var('g', self.app.get_setting('med_g', 'slider'))
        self.app.indicators_frame.g_indicator.update()
        self.app.after(1000, lambda: self.app.set_var('g', self.app.get_setting('high_g', 'slider')))
        self.app.after(1010, lambda: self.app.indicators_frame.g_indicator.update())
        self.app.after(2200, lambda: self.app.set_var('g', self.app.get_setting('over_g', 'slider')))
        self.app.after(2210, lambda: self.app.indicators_frame.g_indicator.update())     
        self.app.after(3200, lambda: self.app.set_var('g', int(self.app.get_setting('over_g','slider')/10)))
        self.app.after(3210, lambda: self.app.indicators_frame.g_indicator.update())
        self.app.after(3210, lambda: self.app.set_var('audio_testing', False))

class AoAVolumeSlider(VolumeSlider):
    def button_event(self):
        self.app.set_var('audio_testing', True)
        self.app.set_var('aoa', self.app.get_setting('high_aoa', 'slider'))
        self.app.indicators_frame.aoa_indicator.update()
        self.app.after(1000, lambda: self.app.set_var('aoa', int(self.app.get_setting('high_aoa','slider')*2/10)))
        self.app.after(1010, lambda: self.app.indicators_frame.aoa_indicator.update())
        self.app.after(1010, lambda: self.app.set_var('audio_testing', False))
        