from sqlalchemy.orm import Session

from app.models.video_project import VideoProject
from app.schemas.video_project import VideoProjectCreate


def get_all_video_projects(db: Session) -> list[VideoProject]:
    return db.query(VideoProject).order_by(VideoProject.created_at.desc()).all()


def create_video_project(
    db: Session,
    project_data: VideoProjectCreate,
) -> VideoProject:
    project = VideoProject(**project_data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project