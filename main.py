#Audio input and test 5s delay
import sounddevice as sd
import numpy as np 
from pylab import*
import matplotlib.pyplot as plt
from scipy.io import wavfile
import speech_recognition as sr
import os
#The audio can have an action and an object(eg-file)
action=""
obj=""
duration = 5
fs=16000
N=int(duration*fs)

text=input('Press enter whenever you are ready-')
while(True):
	if text =="":
		break
	
while(True):
	
		
	data = sd.rec(int(duration*fs),samplerate=fs,channels=1)
	sd.wait()
#freq =(fft((data)))
#w=np.linspace(0,fs/2,num=N/2)
#plt.plot(w,(abs(freq[:N//2])))
#plt.plot(data)
#plt.show()


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
		continue



#Asking permissions for running command through command terminal

#Identifying action and object

	obj_lst=["desktop",'documents','music','sound','volume','audio','screen','calculator','brightness','time','date','calendar','file','folder','google','downloads','firefox']
	action_lst=['make','copy','go','to','open','move','increase','decrease','mute','reduce','unmute']

	for i in text.split():
		i=i.lower()
		if i in obj_lst:
			obj= i
		if i in action_lst:
			action=i

	obj=obj.strip()
	action=action.strip()
#NAVIGATION
	if (action == "go" or "open" or'to'):	
		if obj == "desktop":
			os.system("gnome-open /home/bala/Desktop")
		if obj == 'documents':
			os.system("gnome-open /home/bala/Documents")
		if obj == 'music':
			os.system("gnome-open /home/bala/Music")
		if obj == 'downloads':
			os.system("gnome-open /home/bala/Downloads")
		if obj == 'pictures':
			os.system("gnome-open /home/bala/Pictures")
		if obj == 'calculator':
			os.system("gnome-calculator")
		if obj== 'firefox':
			os.system("firefox")
#SOUND SETTINGS
	if obj == 'volume' or 'audio':
		if action == 'increase':
			os.system("amixer set 'Master' 10%+")
		if action == 'decrease' or 'reduce':
			os.system("amixer set 'Master' 10%-")
		if action == 'mute':
			os.system("amixer set 'Master' mute")		
		if action == 'unmute':
			os.system("amixer set 'Master' unmute")
