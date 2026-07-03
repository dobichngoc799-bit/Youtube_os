from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class VideoProject(Base):
    __tablename__ = "video_projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=True)
    target_length: Mapped[str] = mapped_column(String(50), nullable=True)
    keyword: Mapped[str] = mapped_column(String(255), nullable=True)

    status: Mapped[str] = mapped_column(String(50), default="idea")

    views: Mapped[int] = mapped_column(Integer, default=0)
    ctr: Mapped[float] = mapped_column(Float, default=0.0)
    retention: Mapped[float] = mapped_column(Float, default=0.0)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )