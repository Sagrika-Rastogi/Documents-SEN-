
import speech_recognition as sr
import pyaudio

print("Hello")
r = sr.Recognizer()

with sr.Microphone(sample_rate = 16000) as source:
	audio = r.listen(source)	

print("Listening")
 

try:
	hellos = r.recognize_google(audio)
	print("you said " + hellos)
except LookupError:
	print("Couldn't understand audio")


dummy1 = open('dummy.txt','a')


dummy1.write(hellos)


