from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def dashboard(request: Request):
    stats = {
        "total_projects": 0,
        "published_videos": 0,
        "in_progress": 0,
        "avg_ctr": "0.0%",
    }

    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "page_title": "Dashboard",
            "stats": stats,
        },
    )