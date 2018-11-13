#!/usr/lib/python3.6/
import speech_recognition as sr
AUDIO_FILE = ("example.wav")
# use the sudio file as the audio source
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
	#reads the audio file. here we use record instead of
	#listen
	audio=r.record(source)

try:
	print('the audio file contains:' + r.recognize_google(audio))
except  sr.UnknownValueError:
	print("Google speech recognition could not ")
except sr.RequestError as e:
	print("could not request rsults from google speech recognition service;{0}".forma)