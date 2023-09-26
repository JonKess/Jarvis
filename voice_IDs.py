import pyttsx3

# Initialize the text-to-speech engine with a male voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Print out available voices
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id, voice.name)
