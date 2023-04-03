# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
import sys

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

def getText():
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			print("Say something!")
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input
			audio2 = r.listen(source2)
			print(audio2.get_wav_data)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()
			sys.stdout.write("\r%s" % (MyText))
			return MyText
			
	except sr.RequestError as e:
		raise Exception("Could not request results; {0}".format(e))
		# print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		raise Exception("unknown error occurred")
		# print("unknown error occurred")
	
	
# Loop infinitely for user to
# speak
obj = ['metal', 'apple', 'can']
while(1):
	i = int(input("\nEnter 1 for voice command :- "))
	if i==1:
		text = getText()

		ls = text.split(" ")

		# print(ls)

		if "pickup" in ls:
			avaliable = False
			for i in obj:
				if i in ls:
					# Code for pick that object
					avaliable = True
					pass
			if not avaliable:
				print("Didn't get any object in input, try again")
			
		elif "drop" in ls:
			# Code to drop the object hold by arm
			pass
		else:
			print("Invalid input")
			



