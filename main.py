#Audio input and test 5s delay
import sounddevice as sd
import numpy as np 
from pylab import*
import matplotlib.pyplot as plt
from scipy.io import wavfile
import speech_recognition as sr
import os
duration = 5
fs=16000
N=int(duration*fs)
text=input('Press enter whenever you are ready-')
while(True):
	if text =="":
		break
	
data = sd.rec(int(duration*fs),samplerate=fs,channels=1)
sd.wait()
freq =(fft((data)))
w=np.linspace(0,fs/2,num=N/2)
plt.plot(w,(abs(freq[:N//2])))
#plt.plot(data)
plt.show()


y = (np.iinfo(np.int32).max*(data/np.abs(data).max())).astype(np.int32)
wavfile.write("input.wav", fs, y)
AUDIO= ("input.wav")
r= sr.Recognizer()
with sr.AudioFile(AUDIO) as source:
	audio = r.record(source)
	
#Detecting text using speech processing
text=""
try:
	print("The audio file contains: "+ r.recognize_google(audio))
	text =r.recognize_google(audio)
except sr.UnknownValueError:
	print("Couldn't recognize")
	



#Asking permissions for running command through command terminal

#Using it to either increase / decrease sound

if 'increase' in text and 'volume' in text:
	os.system("amixer set 'Master' 10%+")


if 'decrease' in text and 'volume' in text:
	os.system("amixer set 'Master' 10%-")


if 'increase' in text and 'volume' in text:
	os.system("amixer set 'Master' 10%+")

