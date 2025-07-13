from fastapi import FastAPI
from .routers import courses

app = FastAPI(title="ASU Course Planner API")

app.include_router(courses.router, prefix="/courses", tags=["courses"])

@app.get("/ping")
def ping():
    return {"status": "ok"}
