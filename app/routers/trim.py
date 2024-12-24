import os
import uuid

import moviepy as mp
from config import config
from database import get_session_local
from fastapi import APIRouter, Depends, HTTPException
from models import Video
from sqlalchemy.orm import Session

router = APIRouter(prefix="/trim", tags=["trim"])


@router.post("/{video_id}")
def trim_video(
    video_id: str,
    start_time: int,
    end_time: int,
    db: Session = Depends(get_session_local),
):
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    clip = mp.VideoFileClip(video.filepath)
    trimmed_clip = clip.subclipped(start_time, end_time)
    trimmed_file_path = os.path.join(
        f"./{config.UPLOAD_DIR}", f"trimmed_{uuid.uuid4()}.mp4"
    )
    trimmed_clip.write_videofile(trimmed_file_path, codec="libx264")
    video = Video(
        id=str(uuid.uuid4()), filename=video.filename, filepath=trimmed_file_path
    )
    db.add(video)
    db.commit()

    return {"message": "Video trimmed successfully", "video_id": video.id}
