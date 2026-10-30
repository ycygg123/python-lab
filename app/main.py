from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import Note, engine

app = FastAPI()


class NoteIn(BaseModel):
    title: str
    content: str = ""

class NoteOut(BaseModel):
    model_config = {"from_attributes": True}


    id: int
    title: str
    content: str

def get_session():
    with Session(engine) as session:
        yield session


@app.post("/notes")
def create_note(payload: NoteIn, session: Session = Depends(get_session)):
    note = Note(title=payload.title, content=payload.content)
    session.add(note)
    session.commit()
    session.refresh(note)
    return {"id": note.id, "title": note.title, "content": note.content}

@app.get("/notes/{note_id}",response_model=NoteOut)
def get_all_notes(note_id: int,session: Session = Depends(get_session)):
    note = session.get(Note,note_id)
    if not note:
        raise HTTPException(status_code=404,detail="该条笔记不存在！")
    return note

@app.get("/notes", response_model=list[NoteOut])
def list_notes(session: Session = Depends(get_session)):
    return session.scalars(select(Note)).all()

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int,session: Session = Depends(get_session)):
    note = session.get(Note,note_id)
    if not note:
        raise HTTPException(status_code=404, detail="该笔记不存在！")
    session.delete(note)
    session.commit()
    