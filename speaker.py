import pyttsx3

def speak(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    # You can adjust the rate, volume, and voice properties as needed
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # You can change the voice here
    
    # Speak the text
    engine.say(text)
    
    # Wait for the speech to finish
    engine.runAndWait()

# Example usage:

