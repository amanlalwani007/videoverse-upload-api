import os
from tempfile import NamedTemporaryFile

from config.config import MAX_DURATION_SEC, MAX_FILE_SIZE_MB, MIN_DURATION_SEC
from fastapi.exceptions import HTTPException
from moviepy import VideoFileClip


def validate_video(file):
    file.file.seek(0, os.SEEK_END)  # Move the cursor to the end of the file
    file_size = file.file.tell()  # Get the cursor position (file size in bytes)
    file.file.seek(0)  # Reset the cursor to the beginning
    max_size_bytes = MAX_FILE_SIZE_MB * 1024 * 1024
    if file_size > max_size_bytes:
        raise HTTPException(
            status_code=400, detail=f"File size exceeds {MAX_FILE_SIZE_MB} MB limit."
        )

    with NamedTemporaryFile(delete=True, suffix=".mp4") as temp_file:
        temp_file.write(file.file.read())
        temp_file.flush()
        clip = VideoFileClip(temp_file.name)
        duration = clip.duration
        clip.close()
        if duration > MAX_DURATION_SEC or duration < MIN_DURATION_SEC:
            raise HTTPException(
                status_code=400,
                detail=f"Video duration exceeds {MAX_DURATION_SEC}  or less than {MIN_DURATION_SEC} seconds limit.",
            )
