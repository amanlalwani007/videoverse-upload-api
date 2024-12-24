import os
import uuid

from config import config
from database import get_session_local
from fastapi import APIRouter, Depends, UploadFile
from models import Video
from sqlalchemy.orm import Session
from utils.video_processing import validate_video

router = APIRouter(prefix="/upload", tags=["upload"])
UPLOAD_DIR = f"./{config.UPLOAD_DIR}"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
def upload_video(file: UploadFile, db: Session = Depends(get_session_local)):
    validate_video(file)
    file.file.seek(0)
    file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{file.filename}")
    with open(file_path, "wb") as buffer:
        content = file.file.read()
        buffer.write(content)
    video = Video(id=str(uuid.uuid4()), filename=file.filename, filepath=file_path)
    db.add(video)
    db.commit()
    return {"message": "Video uploaded successfully", "video_id": video.id}
