import speech_recognition as sr
from requestToGPT import gpt
from gtts import gTTS
from playsound import playsound
import pyaudio

# Get the default audio device
p = pyaudio.PyAudio()
default_device_index = p.get_default_input_device_info()['index']

r = sr.Recognizer()
mic = sr.Microphone(default_device_index)

# Adjust the energy threshold for ambient noise levels
with mic as source:
    r.adjust_for_ambient_noise(source)

# Start listening for voice commands
while True:
    print("Listening for voice commands...")
    with mic as source:
        audio = r.listen(source)
    try:
        # Convert the audio to text and print the result
        command = r.recognize_google(audio)
        print(command)
        print("You said: " + command)
        # Create a gTTS object for the text
        response = gpt(command)
        # tts = gTTS(gpt(command))
        # # Save the synthesized audio to a file
        # tts.save("output.mp3")
        # playsound("output.mp3")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        #    `` print("Error accessing the service: {0}".format(e))
        pass
