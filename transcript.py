import whisper
import torch
import torchaudio
import torchaudio.transforms as T

def speech2text(audio, sample_rate):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = whisper.load_model("models/base.pt", device=device)
    
    # Resamplage de l'audio / convertissage
    resampler = T.Resample(orig_freq=sample_rate, new_freq=16000)
    audio_16khz = resampler(audio)
    audio_mono = audio_16khz.mean(dim=0, keepdim=True)
    
    # transcription (uniquement le texte est retourné)
    transcript = model.transcribe(audio_mono.squeeze(0), language="fr")
    
    return transcript["text"]