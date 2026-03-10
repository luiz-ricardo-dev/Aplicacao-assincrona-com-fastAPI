from datetime import datetime, UTC
from fastapi import APIRouter, Cookie, status, Header
from typing_extensions import Annotated
from pydantic import BaseModel
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")

fake_db = [
        {"title": f"Criando uma aplicação com Django","date": datetime.now(UTC), 'published': True},
        {"title": f"Primeiros passos com Django","date": datetime.now(UTC), 'published': True},
        {"title": f"Deploy de aplicações Django","date": datetime.now(UTC), 'published': True},
        {"title": f"Deploy de aplicações Django","date": datetime.now(UTC), 'published': True}
]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post

@router.get("/", response_model=list[PostOut])
def read_posts(published: bool, limit: int, skip: int = 0, ads_id: Annotated[str|None, Cookie()] = None,
 user_agent: Annotated[str|None, Header()]= None):
    #def read_posts(skip: int=0, limit=len(fake_db), published: bool = True):
    print(f"Cookie: {ads_id}")
    print(f"Agent-user: {user_agent}")
    return [post for post in fake_db[skip : skip + limit] if post['published'] is published]
  # posts = []
   #for post in fake_db:
    #if len(posts) == limit:
     #   break
    
    #if post['published'] is published:
     #   posts.append(post)
    #
    #eturn posts

@router.get("/{framework}", response_model=PostOut)
def read_framwork_posts(framework):
    return {"posts": [
        {"title": f"Criando uma aplicação com {framework}","date": datetime.now(UTC)},
        {"title": f"Primeiros passos com {framework}","date": datetime.now(UTC)},
        {"title": f"Deploy de aplicações {framework}","date": datetime.now(UTC)}
    ]}
