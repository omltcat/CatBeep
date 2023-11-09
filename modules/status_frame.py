import customtkinter

class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.app = self.master

        self.status_label = customtkinter.CTkLabel(self, text=self.app.text['status']['not_running'])
        self.status_label.grid(padx=10, pady=0)

    def update_text(self, status):
        self.status_label.configure(text=self.app.text['status'][status])