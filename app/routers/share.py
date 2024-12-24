import uuid
from datetime import datetime, timedelta

from database import get_session_local
from fastapi import APIRouter, Depends, HTTPException
from models import SharedLink, Video
from sqlalchemy.orm import Session

router = APIRouter(prefix="/share", tags=["share"])


@router.post("/{video_id}")
def share_video(
    video_id: str, expiry_minutes: int, db: Session = Depends(get_session_local)
):
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    expiry_time = datetime.utcnow() + timedelta(minutes=expiry_minutes)
    shared_link = SharedLink(
        id=str(uuid.uuid4()), video_id=video.id, expiry_time=expiry_time
    )
    db.add(shared_link)
    db.commit()

    return {
        "shared_link": f"/download/{shared_link.id}",
        "expires_at": shared_link.expiry_time,
    }
