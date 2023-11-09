import tkinter
import customtkinter
import json, yaml

# Functions
def set_language(choice, init=False):
    global text
    if choice in ['中文', 'cn']:
        settings['UI']['language'] = 'cn'
    else:
        settings['UI']['language'] = 'en'
    with open(f"lang/{settings['UI']['language']}.yaml", 'r', encoding='utf-8') as text_file:
        text = yaml.safe_load(text_file)
    if not init:
        status_label.configure(text=text['status']['lang_restart'])
        with open('config/settings.json', 'w', encoding='utf-8') as settings_file:
            json.dump(settings, settings_file, indent=4, ensure_ascii=False)

def checkbox_event_high_g():
    print("checkbox toggled, current value:", high_g_checkbox_value.get())

def start_button_event():
    print("start button pressed")
    

# System settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("640x480")
app.grid_columnconfigure((0), weight=1)
app.grid_columnconfigure((1), weight=1)

# Layout
options_frame = customtkinter.CTkFrame(app)
options_frame.grid(row=0, column=0, padx=(10,5), pady=10, sticky="nsew")
options_frame.grid_columnconfigure((0,1), weight=1)

indicator_frame = customtkinter.CTkFrame(app)
indicator_frame.grid(row=0, column=1, padx=(5,10), pady=10, sticky="nsew")
indicator_frame.grid_columnconfigure((0,1), weight=1)
# indicator_frame.configure(fg_color="transparent")


status_frame = customtkinter.CTkFrame(app)
status_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(0,10), sticky="sew")
# status_frame.configure(fg_color="transparent")


# Load settings
with open('config/settings.json', 'r', encoding='utf-8') as settings_file:
    settings = json.load(settings_file)
text = 'good'
set_language(settings['UI']['language'], init=True)
app.title(text['title'])

# Settings options
lang_label = customtkinter.CTkLabel(options_frame, text=text['label']['language'], fg_color="transparent")
lang_menu = customtkinter.CTkOptionMenu(master=options_frame,
                                       values=["中文", "English"],
                                       command=set_language)
lang_menu.set(text['current_lang'])  # set initial value

lang_label.grid(row=0, column=0, padx=(50,0), pady=(10,5), sticky="w")
lang_menu.grid(row=0, column=1, padx=(0,10), pady=(10,10))

med_g_checkbox_value = customtkinter.StringVar(value=settings['alarms']['med_g']['checkbox'])
med_g_checkbox = customtkinter.CTkCheckBox(options_frame, text=text['checkbox']['med_g'], command=checkbox_event_high_g, variable=med_g_checkbox_value, onvalue="on", offvalue="off")
med_g_checkbox.grid(row=1, column=0, padx=(20,0), pady=5, sticky="w")
med_g_entry_value = customtkinter.StringVar(value="7.0")
med_g_entry = customtkinter.CTkEntry(options_frame, textvariable=med_g_entry_value)
med_g_entry.grid(row=1, column=1, padx=(0,10), pady=5)

high_g_checkbox_value = customtkinter.StringVar(value=settings['alarms']['high_g']['checkbox'])
high_g_checkbox = customtkinter.CTkCheckBox(options_frame, text=text['checkbox']['high_g'], command=checkbox_event_high_g, variable=high_g_checkbox_value, onvalue="on", offvalue="off")
high_g_checkbox.grid(row=2, column=0, padx=(20,0), pady=5, sticky="w")
high_g_entry_value = customtkinter.StringVar(value="7.0")
high_g_entry = customtkinter.CTkEntry(options_frame, textvariable=high_g_entry_value)
high_g_entry.grid(row=2, column=1, padx=(0,10), pady=5)

over_g_checkbox_value = customtkinter.StringVar(value=settings['alarms']['over_g']['checkbox'])
over_g_checkbox = customtkinter.CTkCheckBox(options_frame, text=text['checkbox']['over_g'], command=checkbox_event_high_g, variable=over_g_checkbox_value, onvalue="on", offvalue="off")
over_g_checkbox.grid(row=3, column=0, padx=(20,0), pady=5, sticky="w")
over_g_entry_value = customtkinter.StringVar(value="7.0")
over_g_entry = customtkinter.CTkEntry(options_frame, textvariable=over_g_entry_value)
over_g_entry.grid(row=3, column=1, padx=(0,10), pady=5)

high_aoa_checkbox_value = customtkinter.StringVar(value=settings['alarms']['high_aoa']['checkbox'])
high_aoa_checkbox = customtkinter.CTkCheckBox(options_frame, text=text['checkbox']['high_aoa'], command=checkbox_event_high_g, variable=high_aoa_checkbox_value, onvalue="on", offvalue="off")
high_aoa_checkbox.grid(row=4, column=0, padx=(20,0), pady=5, sticky="w")
high_aoa_entry_value = customtkinter.StringVar(value="10.0")
high_aoa_entry = customtkinter.CTkEntry(options_frame, textvariable=high_aoa_entry_value)
high_aoa_entry.grid(row=4, column=1, padx=(0,10), pady=5)

start_button = customtkinter.CTkButton(options_frame, text=text['button']['start'])
start_button.grid(row=5, column=0, columnspan=2, padx=(20,20), pady=(20,10), sticky="ew")

# Indicators
g_meter = customtkinter.CTkProgressBar(indicator_frame, orientation="vertical", border_width=2, corner_radius=0, width=80, progress_color="green")
g_meter.set(0.3)
g_meter.grid(row=0, column=0, padx=(20,10), pady=10, sticky="nsew")
g_label = customtkinter.CTkLabel(indicator_frame, text=text['label']['g_load'])
g_label.grid(row=1, column=0, padx=(20,10), pady=(0,10), sticky="ew")

aoa_meter = customtkinter.CTkProgressBar(indicator_frame, orientation="vertical", border_width=2, corner_radius=0, width=80, progress_color="green")
aoa_meter.set(0.3)
aoa_meter.grid(row=0, column=1, padx=(10,20), pady=10, sticky="nsew")
aoa_label = customtkinter.CTkLabel(indicator_frame, text=text['label']['aoa'])
aoa_label.grid(row=1, column=1, padx=(10,20), pady=(0,10), sticky="ew")

# Status text
status_label = customtkinter.CTkLabel(status_frame, text=text['status']['not_running'])
status_label.grid(padx=10, pady=0)
# Pack widgets

# Run app
app.mainloop()
