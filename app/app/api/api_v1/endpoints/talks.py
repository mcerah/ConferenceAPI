from fastapi import APIRouter, Depends, HTTPException
from app.models.talk import Talk, TalkCreate, TalkUpdate
from app.models.person import Person
from app.api import deps
from typing import Optional

router = APIRouter()


@router.get("/{talk_id}")
def get_talk(talk_id: int, session: deps.Session = Depends(deps.get_session)):
    db_talk = session.get(Talk, talk_id)
    if not db_talk:
        raise HTTPException(status_code=404, detail="Talk not found")
    return db_talk


@router.get("/")
def get_talks(conference_id: Optional[int] = None, session: deps.Session = Depends(deps.get_session)):
    if conference_id is not None:
        statement = deps.select(Talk).where(
            Talk.conference_id == conference_id)
    else:
        statement = deps.select(Talk)

    talks = session.exec(statement).all()
    return talks


@router.post("/")
def create_talk(talk: TalkCreate, session: deps.Session = Depends(deps.get_session)):

    speakers = session.exec(deps.select(Person).where(
        Person.id.in_(talk.speakers))).all()
    participants = session.exec(deps.select(Person).where(
        Person.id.in_(talk.participants))).all()

    talk = Talk(title=talk.title, description=talk.description,
                duration=talk.duration, date_time=talk.date_time, conference_id=talk.conference_id, speakers=speakers, participants=participants)

    session.add(talk)
    session.commit()
    session.refresh(talk)
    return talk


@router.patch("/{talk_id}")
def update_talk(talk_id: int, talk: TalkUpdate, session: deps.Session = Depends(deps.get_session)):
    db_talk = session.get(Talk, talk_id)
    if not db_talk:
        raise HTTPException(status_code=404, detail="Talk not found")

    speakers = session.exec(deps.select(Person).where(
        Person.id.in_(talk.speakers))).all()
    participants = session.exec(deps.select(Person).where(
        Person.id.in_(talk.participants))).all()

    talk_data = talk.dict(exclude_unset=True)
    for key, value in talk_data.items():
        if key == "speakers":
            setattr(db_talk, key, speakers)
        elif key == "participants":
            setattr(db_talk, key, participants)
        else:
            setattr(db_talk, key, value)

    session.add(db_talk)
    session.commit()
    session.refresh(db_talk)

    return db_talk
