from pydantic import BaseModel
from datetime import datetime, UTC

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: datetime | None
 