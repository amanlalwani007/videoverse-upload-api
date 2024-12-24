import os
import uuid

import moviepy as mp
from config import config
from database import get_session_local
from fastapi import APIRouter, Depends, HTTPException
from models import Video
from sqlalchemy.orm import Session

router = APIRouter(prefix="/merge", tags=["merge"])


@router.post("/")
def merge_videos(video_ids: list[str], db: Session = Depends(get_session_local)):
    clips = []
    video_names = []
    for video_id in video_ids:
        video = db.query(Video).filter(Video.id == video_id).first()
        if not video:
            raise HTTPException(
                status_code=404, detail=f"Video with ID {video_id} not found"
            )
        video_names.append(video.filename)    
        clips.append(mp.VideoFileClip(video.filepath))

    merged_clip = mp.concatenate_videoclips(clips)
    merged_file_path = os.path.join(
        f"./{config.UPLOAD_DIR}", f"merged_{uuid.uuid4()}.mp4"
    )
    merged_clip.write_videofile(merged_file_path, codec="libx264")
    filename = "merge_" + "_".join(video_names)
    video = Video(
        id=str(uuid.uuid4()), filename=filename, filepath=merged_file_path
    )
    db.add(video)
    db.commit()

    return {
        "message": "Videos merged successfully",
        "video_id": video.id,
    }
