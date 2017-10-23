# uses my model library - result is faster

#!/usr/bin/env python

def speech_recognition():
  
    # Speech recognition libraries
    from os import environ, path

    from pocketsphinx.pocketsphinx import *
    from sphinxbase.sphinxbase import *

    # Paths for model library files
    MODELDIR = "/usr/local/share/pocketsphinx/model"
    DATADIR = "/home/pi/Desktop/LittleViking"

    # Create a decoder with certain model
    config = Decoder.default_config()
    config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
    config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us/1175.lm'))
    config.set_string('-dict', path.join(MODELDIR, 'en-us/en-us/1175.dic'))
    
    # Decode streaming data.
    decoder = Decoder(config)
    decoder.start_utt()
    stream = open(path.join(DATADIR, 'test.wav'), 'rb')
    while True:
      buf = stream.read(1024)
      if buf:
        decoder.process_raw(buf, False, False)
      else:
        break
    decoder.end_utt()
    #print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])

    hypothesis = decoder.hyp()
    
    if hypothesis != None:
        bestGuess = hypothesis.hypstr
    else:
        bestGuess = "nope"

    #print str(bestGuess)
    if 'LEFT' in bestGuess or 'RIGHT' in bestGuess or 'UP' in bestGuess or 'DOWN' in bestGuess or 'ViCKY' or 'What is your name':
        return str(bestGuess)
    else:
        return "nope"

    #recorder
def record_voice():

    #add voice recording libraries 
    import wave
    import pyaudio

    # Sound file specs
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 2
    
    fn = "test.wav";
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(fn, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    wavfile = fn

