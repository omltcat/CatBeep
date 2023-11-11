import time, json
def watchdog(app):
    app.save_settings()
    old_settings = json.dumps(app.settings)
    old_status = app.get_var('status')
    i = 0
    while True:
        time.sleep(0.1)
        status = app.get_var('status')
        if status not in ['lang_restart', 'no_audio_device']:
            if time.time() - app.get_var('last_received') < 0.2:
                app.set_var('audio_can_play', True)
                app.set_var('status', 'running')
            elif app.get_var('audio_testing'):
                app.set_var('audio_can_play', True)
                app.set_var('status', 'audio_testing')
            else:    
                app.set_var('audio_can_play', False)
                app.set_var('status', 'idle')
            
            if status != old_status:
                old_status = status
                app.status_frame.update_text()

            i += 1
            if i == 10:
                i = 0
                if json.dumps(app.settings) != old_settings:
                    print("new saved")
                    app.save_settings()
                    old_settings = json.dumps(app.settings)