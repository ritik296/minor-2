import tkinter as tk
import speech_recognition as sr

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Input Press-and-Hold")
        self.master.geometry("800x600")

        # Create a label for the list of objects
        self.objects_label = tk.Label(self.master, text="List of objects:")
        self.objects_label.pack(pady=(20, 0))

        # Create a list of objects
        self.objects = ["apple", "banana", "orange", "pear", "grape"]

        # Create a listbox to display the objects
        self.objects_listbox = tk.Listbox(self.master, width=40)
        self.objects_listbox.pack(pady=(5, 20))

        # Add the objects to the listbox
        for obj in self.objects:
            self.objects_listbox.insert(tk.END, obj.capitalize())

        self.console_text = tk.Text(self.master, width=50, height=10, bg="#1E1E1E", fg="white", bd=0, highlightthickness=0)
        self.console_text.pack(pady=(0, 20))

        # Create a button to start voice input
        self.voice_input_button = tk.Button(self.master, text="Press and Hold to Speak", font=("Arial", 14), command=self.start_voice_input, bd=0, relief=tk.RIDGE)
        self.voice_input_button.pack(pady=(0, 20))

        # Create a label for the microphone icon
        self.mic_label = tk.Label(self.master, text="", font=("FontAwesome", 30))
        self.mic_label.pack(pady=(0, 10))

        # Set the microphone icon to the inactive state
        self.mic_label.config(text="\uf130", fg="gray")

        # Initialize the speech recognition module
        self.r = sr.Recognizer()

        # Set the initial state of the voice input button
        self.voice_input_enabled = False

    def start_voice_input(self):
        # Set the state of the voice input button
        self.voice_input_enabled = True

        # Change the button text and color, and show the microphone icon
        self.voice_input_button.config(text="Speaking...", bg="#f9b384", fg="white")
        self.mic_label.config(text="\uf130", fg="#f9b384")

        # Use the microphone as the audio source
        with sr.Microphone() as source:
            self.console_text.insert(tk.END, "Toggle voice command!\n")
            print("Say something!")
            audio = self.r.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = self.r.recognize_google(audio)
            self.console_text.insert(tk.END, "Google Speech Recognition thinks you said: " + text + "\n")
            print("Google Speech Recognition thinks you said: " + text)

            # Check if the recognized text matches an object in the list
            if any(obj in text.lower() for obj in self.objects):
                # Call the pickup function for the recognized object
                self.pickup(text.lower())

            # Check if the recognized text contains "drop"
            elif "drop" in text.lower():
                # Call the drop function
                self.drop()

            else:
                self.console_text.insert(tk.END, "Didn't get any object" + "\n")
                print("Didn't get any object")

        except sr.UnknownValueError:
            self.console_text.insert(tk.END, "Google Speech Recognition could not understand audio" + "\n")
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            self.console_text.insert(tk.END, "Could not request results from Google Speech Recognition service; {0}".format(e) + "\n")
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        # Set the state of the voice input button
        self.voice_input_enabled = False

        # Change the button text and color, and hide the microphone icon
        self.voice_input_button.config(text="Press and Hold to Speak", bg="white", fg="black")
        self.mic_label.config(text="\uf130", fg="gray")

    def pickup(self, st):
        self.console_text.insert(tk.END, f"Picking {st}" + "\n")
        print(f"Picking {st}")
    
    def drop(self):
        self.console_text.insert(tk.END, "Droping object" + "\n")
        print("Droping object")

   
root = tk.Tk()
app = App(root)
root.mainloop()