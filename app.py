import streamlit as st
import requests
import subprocess
import time
import signal

#Interface web

st.set_page_config(
    page_title="Transcription automatique de la parole",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="auto",
)

# Fonction pour démarrer le serveur FastAPI
def start_fastapi_server():
    process = subprocess.Popen(["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"])
    return process

# Fonction pour arrêter le serveur FastAPI
def stop_fastapi_server(process):
    process.send_signal(signal.SIGINT)
    process.wait()

# gestionnaire de contexte pour démarrer et arrêter le serveur FastAPI
class FastAPIServer:
    def __enter__(self):
        self.process = start_fastapi_server()
        return self.process

    def __exit__(self, exc_type, exc_val, exc_tb):
        stop_fastapi_server(self.process)

@st.cache_data(persist=True, show_spinner=True)
def process_audio(audio_file):
    response = requests.post(
        "http://localhost:8000/transcription",
        files={"file": (audio_file.name, audio_file, audio_file.type)}
    )
    if response.status_code == 200:
        return response.json().get("transcript", "pas de transcript trouvé dans le réponse.")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

st.title("Transcription automatique de la parole (fr)")
st.info('Formats supportés - WAV, MP3, MP4, OGG, WMA, AAC, FLAC, FLV ')
uploaded_file = st.file_uploader("Upload audio file", type=["wav", "mp3", "ogg", "wma", "aac", "flac", "mp4", "flv"])

if uploaded_file is not None:
    st.markdown("---")
    st.markdown("Lecture du fichier audio")
    st.audio(uploaded_file)

    if st.button("Génération de la transcription"):
        with st.spinner(f"Génération de la transcription en cours... "):
            transcript = process_audio(uploaded_file)
            if transcript:
                st.markdown("### Transcription")
                st.text_area("Transcription", transcript, height=200)
                st.balloons()
                st.success('Transcription générée avec succès ')

# Démarrer le serveur FastAPI et l'exécuter en continu
start_fastapi_server()
st.write("FastAPI server is running...")