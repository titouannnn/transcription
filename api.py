from transcript import speech2text
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import torch
import torchaudio
import io
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/transcription")
async def upload_file(file: UploadFile):
    try:
        audio_bytes = await file.read()
        audio_tensor, sample_rate = torchaudio.load(io.BytesIO(audio_bytes))
        
        logger.info(f"Audio tensor shape: {audio_tensor.shape}, Sample rate: {sample_rate}")
        
        transcript = speech2text(audio_tensor, sample_rate)
        return JSONResponse(content={"transcript": transcript})
    except Exception as e:
        logger.error(f"Error processing file: {e}")
        raise HTTPException(status_code=500, detail=str(e))