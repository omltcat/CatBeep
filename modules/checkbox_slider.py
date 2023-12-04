import customtkinter
import modules.message_box as message_box

class CheckBoxSlider():
    def __init__(self, master, name, row, pady=(20,0), limits=(0,120), unit=" G", blockers=(None, None), help=None):
        self.master = master
        self.app = master.app
        self.name = name
        self.row = row
        self.pady = pady        
        self.limits = limits
        self.unit = unit
        self.blockers = blockers

        self.checkbox_value = customtkinter.IntVar(value=self.app.get_setting(self.name, 'checkbox'))
        self.slider_value = customtkinter.IntVar(value=self.app.get_setting(self.name, 'slider'))

        self.checkbox = customtkinter.CTkCheckBox(self.master, text=self.app.get_string('checkbox', self.name), variable=self.checkbox_value, onvalue=1, offvalue=0, command=self.checkbox_event, font=self.app.font)
        self.slider = customtkinter.CTkSlider(self.master, from_=self.limits[0], to=self.limits[1], number_of_steps=limits[1], variable=self.slider_value, width=10, command=self.slide_event)
        self.label = customtkinter.CTkLabel(self.master, text=f"{self.slider_value.get()/10}{self.unit}", font=self.app.font)

        self.checkbox.grid(row=self.row, column=0, padx=(20,0), pady=self.pady, sticky="w")
        self.slider.grid(row=self.row, column=1, padx=(0,20), pady=self.pady, sticky="ew")
        self.label.place(in_=self.slider, anchor="c", relx=-0.1, rely=0.5)

        if help is not None:
            self.help_button = customtkinter.CTkButton(self.master, fg_color='#404040', text="?", width=10, height=10, font=self.app.font, command=lambda: message_box.help(help, self.app))
            self.help_button.place(in_=self.checkbox, anchor="c", relx=1.13, rely=0.5)

    def checkbox_event(self):
        value = self.checkbox_value.get()
        self.app.set_setting(value, self.name, 'checkbox')
    def slide_event(self, value: int):
        lower_blocker = self.app.get_setting(self.blockers[0], 'slider') if self.blockers[0] is not None else -1000
        upper_blocker = self.app.get_setting(self.blockers[1], 'slider') if self.blockers[1] is not None else 1000
        allowed_value = min(max(value, lower_blocker), upper_blocker)
        if allowed_value != value:
            self.slider_value.set(int(allowed_value))
        self.app.set_setting(int(allowed_value), self.name, 'slider')
        self.label.configure(text=f"{allowed_value/10}{self.unit}")