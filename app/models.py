from datetime import datetime

from database import Base
from sqlalchemy import Column, DateTime, String


class Video(Base):
    __tablename__ = "videos"
    id = Column(String, primary_key=True, index=True)
    filename = Column(String, index=True)
    filepath = Column(String, index=True)
    upload_time = Column(DateTime, default=datetime.utcnow)


class SharedLink(Base):
    __tablename__ = "shared_links"
    id = Column(String, primary_key=True, index=True)
    video_id = Column(String, index=True)
    expiry_time = Column(DateTime)
