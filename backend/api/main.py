from fastapi import FastAPI
from api.routes.search import router

app = FastAPI()
app.include_router(router)
