from fastapi import FastAPI
from . import models
from .database import engine

from .routers import login, owner
# Engine Binds all to Create DB based on Model using Engine - Models.Base.metadata.create_all(bind=<engine_name>)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Always route the HTTP methods Respectively
app.include_router(owner.router)
app.include_router(login.router)