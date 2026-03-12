from controllers import post
from fastapi import FastAPI
from database import database, metadata, engine
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)

#@app.on_event("startup")
#async def startup():
#    await database.connect()
    
#@app.on_event("shutdown")
#async def shutdown():
#    await database.disconnect()
