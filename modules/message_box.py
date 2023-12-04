from CTkMessagebox import CTkMessagebox

def help(name, app):
    CTkMessagebox(title=app.get_string('message_box', f'help_{name}_title'), message=str(app.get_string('message_box', f'help_{name}_text')), icon="info", font=app.font)