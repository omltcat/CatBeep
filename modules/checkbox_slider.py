import customtkinter

class CheckBoxSlider():
    def __init__(self, master, name, row, pady=(10,0), limits=(0,120), unit=" G", blockers=(None, None)):
        self.master = master
        self.app = master.app
        self.name = name
        self.row = row
        self.pady = pady        
        self.limits = limits
        self.unit = unit
        self.blockers = blockers

        self.checkbox_value = customtkinter.IntVar(value=self.app.settings[self.name]['checkbox'])
        self.slider_value = customtkinter.IntVar(value=self.app.settings[self.name]['slider'])

        self.checkbox = customtkinter.CTkCheckBox(self.master, text=self.app.text['checkbox'][self.name], variable=self.checkbox_value, onvalue=1, offvalue=0)
        self.slider = customtkinter.CTkSlider(self.master, from_=self.limits[0], to=self.limits[1], number_of_steps=limits[1], variable=self.slider_value, width=10, command=self.slide_event)
        self.label = customtkinter.CTkLabel(self.master, text=f"{self.slider_value.get()/10}{self.unit}")

        self.checkbox.grid(row=self.row, column=0, padx=(20,0), pady=self.pady, sticky="w")
        self.slider.grid(row=self.row, column=1, padx=(0,20), pady=self.pady, sticky="ew")
        self.label.place(in_=self.slider, anchor="c", relx=-0.1, rely=0.5)

    def slide_event(self, value: int):
        lower_blocker = self.app.settings[self.blockers[0]]['slider'] if self.blockers[0] is not None else -1000
        upper_blocker = self.app.settings[self.blockers[1]]['slider'] if self.blockers[1] is not None else 1000
        allowed_value = min(max(value, lower_blocker), upper_blocker)
        if allowed_value != value:
            value = allowed_value
            self.slider_value.set(allowed_value)
        self.app.settings[self.name]['slider'] = allowed_value
        self.label.configure(text=f"{allowed_value/10}{self.unit}")