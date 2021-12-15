import streamlit as st
import sounddevice as sd
import wavio
import threading 
import logging


class StreamLitApp:
  def __init__(self):
    self.SAMPLE_RATE = 44100
    self.mic_queue = []
    self.CHANNELS = 3
    self.x = threading.Thread(target=self.record)
    self.boolean = True


  def callback(self, indata, frames, time, status):
      if status:
          print(status, file=sys.stderr)
      logging.info(indata.copy())

  def record(self):
    with sd.InputStream(samplerate=self.SAMPLE_RATE, channels=self.CHANNELS, callback=self.callback):
        while True:
          if self.boolean:
            break
        
  def stop_mic_recording(self):
    self.boolean = True
    print("Stop button")
    self.x.join()

  def Record_Btn(self):
    self.boolean = False
    self.x.start()

def main():
  s = StreamLitApp()
  if st.button(f"Click to Record"):
    s.Record_Btn()
  if st.button(f"Click to Stop"):
    s.stop_mic_recording()

if __name__ == '__main__':
  main()
