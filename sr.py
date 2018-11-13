#!/usr/bin/python3
#!/usr/include/python3.6  
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source, duration=5)
	r.dynamic_energy_threshold = True
	print("say something !")
	while True:#creating a while loop
		audio = r.listen(source)#listening to microp
		print('you said' + r.recognize_google(audio))