import spacy
import speech_recognition as sr
from spacy.lang.en.stop_words import STOP_WORDS
from pydub import AudioSegment
from gfg import takeCommandHindi

# Load the Spacy model for NLP
nlp = spacy.load("en_core_web_sm")

# Function to transcribe audio to text
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    
    # Load the audio file using pydub
    audio = AudioSegment.from_file(file_path)
    
    # Convert the audio to a format compatible with SpeechRecognition
    audio.export("converted.wav", format="wav")
    audio_file = sr.AudioFile("converted.wav")
    
    with audio_file as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    return text

# Function to remove stop words
def preprocess(text):
    doc = nlp(text)
    no_stop_words = [token.text for token in doc if not token.is_stop]
    return " ".join(no_stop_words)

# Example usage
# audio_file_path = "SIh/Recording.m4a"
# transcribed_text = transcribe_audio(audio_file_path)
transcribed_text = takeCommandHindi()
processed_text = preprocess(transcribed_text)

print("Transcribed Text:", transcribed_text)
print("Processed Text (No Stop Words):", processed_text)
