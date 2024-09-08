# import speech_recognition as sr
# from pydub import AudioSegment
import os

# # Initialize recognizer
# recognizer = sr.Recognizer()

# # Function to convert audio file to text
# def transcribe_audio(audio_path):
#     # Convert to a format recognized by the library if necessary
#     if audio_path.endswith(".mp3"):
#         sound = AudioSegment.from_mp3(audio_path)
#         audio_path = audio_path.replace(".mp3", ".wav")
#         sound.export(audio_path, format="wav")
    
#     # Load audio file
#     with sr.AudioFile(audio_path) as source:
#         audio = recognizer.record(source)  # Read the audio file
        
#     try:
#         # Recognize speech using Google Web Speech API
#         text = recognizer.recognize_google(audio)
#         print(f"Transcription for {audio_path}: {text}")
#     except sr.UnknownValueError:
#         print(f"Google Web Speech API could not understand audio {audio_path}")
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Web Speech API; {e}")

# # Directory containing your audio files
directory = 'audio data/'

# # Loop through all files and transcribe them
# for audio in os.listdir(directory):
#     audio_path = directory + audio
#     transcribe_audio(audio_path)

from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import torch
import librosa

# Load pre-trained model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def transcribe_with_wav2vec(audio_path):
    # Load and preprocess audio file
    audio, rate = librosa.load(audio_path, sr=16000)
    
    # Tokenize input
    input_values = tokenizer(audio, return_tensors="pt").input_values

    # Perform inference
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)

    # Decode the prediction
    transcription = tokenizer.decode(predicted_ids[0])
    print(f"Transcription for {audio_path}: {transcription}")

# Transcribe with Wav2Vec2
for audio in os.listdir(directory):
    transcribe_with_wav2vec(directory + audio)
