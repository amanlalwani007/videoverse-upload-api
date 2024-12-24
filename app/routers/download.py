from datetime import datetime

from database import get_session_local
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from models import SharedLink, Video
from sqlalchemy.orm import Session

router = APIRouter(prefix="/download", tags=["download"])


@router.get("/{link_id}")
def download_video(link_id: str, db: Session = Depends(get_session_local)):
    shared_link = db.query(SharedLink).filter(SharedLink.id == link_id).first()
    if not shared_link or shared_link.expiry_time < datetime.utcnow():
        raise HTTPException(status_code=404, detail="Link expired or invalid")

    video = db.query(Video).filter(Video.id == shared_link.video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    return FileResponse(video.filepath, media_type="video/mp4", filename=video.filename)
