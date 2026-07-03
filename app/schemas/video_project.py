from pydantic import BaseModel


class VideoProjectCreate(BaseModel):
    title: str
    category: str | None = None
    target_length: str | None = None
    keyword: str | None = None
    status: str = "idea"