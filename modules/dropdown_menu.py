import customtkinter
import json, yaml

class DropdownMenu():
    def __init__(self, master, name, row, pady=(10,0)):
        self.master = master
        self.app = master.app
        self.name = name
        self.row = row
        self.pady = pady
       
        self.label = customtkinter.CTkLabel(self.master, text=self.app.text['label'][self.name], fg_color="transparent")
        self.menu = customtkinter.CTkOptionMenu(self.master, command=self.menu_event)

        self.label.grid(row=0, column=0, padx=(50,0), pady=self.pady, sticky="w")
        self.menu.grid(row=0, column=1, padx=(0,10), pady=self.pady)

    # Function called upon selection, change this
    def menu_event(self, value):
        pass
        # print(f"{self.label.cget('text')}: {value}")

class LanguageMenu(DropdownMenu):
    def __init__(self, master, name, row, pady=...):
        super().__init__(master, name, row, pady)

        self.menu.configure(values=["中文", "English"])
        self.menu.set(self.app.text['current_lang'])  # set initial value

    def menu_event(self, value):
        if value in ['中文', 'cn']:
            self.app.settings['language'] = 'cn'
        else:
            self.app.settings['language'] = 'en'
        self.app.read_string_table()
        self.app.save_settings()
        self.app.status_frame.update_text("lang_restart")