import customtkinter

class CheckBoxEntry():
    def __init__(self, master, name, row, pady=(10,0)):
        self.master = master
        self.app = master.app
        self.name = name
        self.row = row
        self.pady = pady

        self.checkbox_value = customtkinter.IntVar(value=self.app.settings[self.name]['checkbox'])
        self.entry_value = customtkinter.StringVar(value=self.app.settings[self.name]['entry'])

        self.checkbox = customtkinter.CTkCheckBox(self.master, text=self.app.text['checkbox'][self.name], variable=self.checkbox_value, onvalue=1, offvalue=0)
        self.entry = customtkinter.CTkEntry(self.master, textvariable=self.entry_value)

        self.checkbox.grid(row=self.row, column=0, padx=(20,0), pady=self.pady, sticky="w")
        self.entry.grid(row=self.row, column=1, padx=(0,10), pady=self.pady)