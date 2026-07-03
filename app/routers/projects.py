from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/projects", tags=["Projects"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def projects_page(request: Request):
    projects = []

    return templates.TemplateResponse(
        request,
        "projects.html",
        {
            "page_title": "Projects",
            "projects": projects,
        },
    )