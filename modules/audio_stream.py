import sounddevice as sd
import soundfile as sf
import threading, time

def g_audio_stream(app):
    sd.default.device = (None, app.get_setting('audio_device', 'id'))
    med_g_data, _ = sf.read('./resources/med_g.wav', dtype='float32')
    high_g_data, _ = sf.read('./resources/high_g.wav', dtype='float32')
    over_g_data, fs = sf.read('./resources/over_g.wav', dtype='float32')
    with sd.OutputStream(channels=1, blocksize=2048, dtype='float32', samplerate=fs) as stream:
        while app.get_var('audio_threads_on'):
            if app.get_var('audio_can_play'):
                if app.get_setting('over_g', 'checkbox') and app.get_var('g') >= app.get_setting('over_g', 'slider'):
                    stream.write(over_g_data*volume(app.get_setting('g_volume')))
                elif app.get_setting('high_g', 'checkbox') and app.get_var('g') >= app.get_setting('high_g', 'slider'):
                    stream.write(high_g_data*volume(app.get_setting('g_volume')))
                elif app.get_setting('med_g', 'checkbox') and app.get_var('g') >= app.get_setting('med_g', 'slider'):
                    stream.write(med_g_data*volume(app.get_setting('g_volume')))
                else:
                    time.sleep(0.05)
            else:
                time.sleep(0.05)

def aoa_audio_stream(app):
    sd.default.device = (None, app.get_setting('audio_device', 'id'))
    data, fs = sf.read('./resources/shaker.wav', dtype='float32')
    with sd.OutputStream(channels=2, blocksize=2048, dtype='float32', samplerate=fs) as stream:
        while app.get_var('audio_threads_on'):
            if app.get_var('audio_can_play'):
                if app.get_setting('high_aoa', 'checkbox') and app.get_var('aoa') >= app.get_setting('high_aoa', 'slider'):
                    stream.write(data*volume(app.get_setting('aoa_volume')))
                else:
                    time.sleep(0.05)
            else:
                time.sleep(0.05)

def volume(vol):
    return (2.7183**(vol/100) - 1)/1.7183