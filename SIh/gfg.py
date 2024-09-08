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
