import spacy
import speech_recognition as sr
from pydub import AudioSegment
from indicnlp.tokenize import indic_tokenize
from indicnlp.normalize.indic_normalize import DevanagariNormalizer
from indicnlp.stopwords import stopwords

# Set the path to the Indic NLP Resources
from indicnlp import common
common.set_resources_path("path_to/indic_nlp_resources")

# Load stop words for Hindi
hindi_stopwords = set(stopwords.get_stopwords('hi'))


INDIC_RESOURCES_PATH = "./indic_nlp_resources"
common.set_resources_path(INDIC_RESOURCES_PATH)


# Load stop words for Hindi
hindi_stopwords = set(stopwords.get_stopwords('hi'))

# Normalizer for Devanagari script (used in Hindi)
normalizer = DevanagariNormalizer()

# Function to transcribe audio to text (Hindi)
def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        audio_data = recognizer.listen(source)
        text = recognizer.recognize_google(audio_data, language='hi-In')
    
    return text

# Function to preprocess Hindi text
def preprocess_hindi_text(text):
    # Normalize the text (remove diacritics, etc.)
    normalized_text = normalizer.normalize(text)

    # Tokenize the text
    tokens = indic_tokenize.trivial_tokenize(normalized_text)

    # Remove stop words
    no_stop_words = [token for token in tokens if token not in hindi_stopwords]
    
    return " ".join(no_stop_words)

# Example usage
transcribed_text = transcribe_audio(takeCommandHindi())
processed_text = preprocess_hindi_text(transcribed_text)

print("Transcribed Text:", transcribed_text)
print("Processed Text (No Stop Words):", processed_text)
