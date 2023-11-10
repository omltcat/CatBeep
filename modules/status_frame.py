import customtkinter

class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.app = self.master
        self.status_dict = self.app.get_string('status')

        self.status_label = customtkinter.CTkLabel(self, font=self.app.font, fg_color="transparent")
        self.status_label.grid(padx=10, pady=0)
        self.update_text()

    def update_text(self, status=None):
        status = self.app.get_var('status') if status is None else status
        text = self.app.get_string('status', status) if status in self.status_dict else status
        self.status_label.configure(text=text)