from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.app.api.routes import router

app = FastAPI(
    title="Exam Score Prediction API",
    version="1.0"
)

# API routes
app.include_router(router)

# Serve frontend
app.mount(
    "/", 
    StaticFiles(directory="src/app/static", html=True),
    name="static"
)