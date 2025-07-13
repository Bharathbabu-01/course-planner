from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3

DB = "courses.db"

class Course(BaseModel):
    id: int
    code: str
    title: str
    credits: int

router = APIRouter()

def _get_conn():
    return sqlite3.connect(DB, check_same_thread=False)

@router.get("/", response_model=List[Course])
def list_courses():
    conn = _get_conn()
    rows = conn.execute("SELECT id, code, title, credits FROM courses").fetchall()
    return [Course(id=r[0], code=r[1], title=r[2], credits=r[3]) for r in rows]
