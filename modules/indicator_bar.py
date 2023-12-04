import customtkinter

class IndicatorBar():
    def __init__(self, master, name, column, padx=(10,10)):
        self.master = master
        self.app = master.app
        self.name = name
        self.column = column
        self.padx = padx

        self.bar = customtkinter.CTkProgressBar(self.master, orientation="vertical", border_width=2, corner_radius=0, width=80, progress_color="green")
        self.bar.grid(row=0, column=self.column, padx=self.padx, pady=(15,0), sticky="nsew")
        self.label = customtkinter.CTkLabel(self.master, text=self.app.get_string('label', self.name), font=self.app.font)
        self.label.grid(row=1, column=self.column, padx=self.padx, pady=(0,10), sticky="s")
        self.update()

    def update(self, value=None):
        self.bar.set(0.3)

class GIndicator(IndicatorBar):
    def update(self, value=None):
        value = self.app.get_var('g') if value is None else value
        threshold_high = self.app.get_setting('high_g', 'slider')
        threshold_med = self.app.get_setting('med_g', 'slider')
        limit = max(1, self.app.get_setting('over_g', 'slider'))

        if value >= threshold_high:
            self.bar.configure(progress_color="red")
        elif value >= threshold_med:
            self.bar.configure(progress_color="yellow")
        else:
            self.bar.configure(progress_color="green")
        
        progress = max(min(value / limit, 1), 0)
        self.bar.set(progress)

class AOAIndicator(IndicatorBar):
    def update(self, value=None):
        value = self.app.get_var('aoa') if value is None else value
        threshold_high = self.app.get_setting('high_aoa', 'slider')
        limit = max(1, threshold_high * 2)
        
        if value >= threshold_high:
            self.bar.configure(progress_color="red")
        else:
            self.bar.configure(progress_color="green")
        
        progress = max(min(value / limit, 1), 0)
        self.bar.set(progress)