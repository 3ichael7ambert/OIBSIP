import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()

# Function to speak a response
def speak(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()

# Function to perform actions based on voice commands
def voice_assistant(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "what's the time" in command:
        # You can use the datetime library to get the current time.
        import datetime
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif "what's the date" in command:
        # You can use the datetime library to get the current date.
        import datetime
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

# Main loop for listening to voice commands
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        voice_assistant(command)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
