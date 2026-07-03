from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.video_project import VideoProjectCreate
from app.services.video_project_service import (
    create_video_project,
    get_all_video_projects,
)

router = APIRouter(prefix="/projects", tags=["Projects"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def projects_page(request: Request, db: Session = Depends(get_db)):
    projects = get_all_video_projects(db)

    return templates.TemplateResponse(
        request,
        "projects.html",
        {
            "page_title": "Projects",
            "projects": projects,
        },
    )


@router.get("/new")
def new_project_page(request: Request):
    return templates.TemplateResponse(
        request,
        "project_form.html",
        {
            "page_title": "New Project",
        },
    )


@router.post("/new")
def create_project(
    title: str = Form(...),
    category: str = Form(""),
    target_length: str = Form(""),
    keyword: str = Form(""),
    status: str = Form("idea"),
    db: Session = Depends(get_db),
):
    project_data = VideoProjectCreate(
        title=title,
        category=category,
        target_length=target_length,
        keyword=keyword,
        status=status,
    )

    create_video_project(db, project_data)

    return RedirectResponse(url="/projects", status_code=303)