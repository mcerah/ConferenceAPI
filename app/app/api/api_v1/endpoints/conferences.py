from fastapi import APIRouter, Depends, HTTPException
from app.models.conference import Conference, ConferenceCreate, ConferenceUpdate
from app.api import deps
from typing import List

router = APIRouter()


@router.get("/{conf_id}", response_model=Conference)
def get_conference(conf_id: int, session: deps.Session = Depends(deps.get_session)):
    db_conf = session.get(Conference, conf_id)
    if not db_conf:
        raise HTTPException(status_code=404, detail="Conference not found")
    return db_conf


@router.get("/")
def get_conferences(session: deps.Session = Depends(deps.get_session)):
    conferences = session.exec(deps.select(Conference)).all()
    return conferences


@router.post("/", response_model=Conference)
def create_conference(conf: ConferenceCreate, session: deps.Session = Depends(deps.get_session)):
    conf = Conference.from_orm(conf)
    session.add(conf)
    session.commit()
    session.refresh(conf)
    return conf


@router.patch("/{conf_id}", response_model=Conference)
def update_conference(conf_id: int, conf: ConferenceUpdate, session: deps.Session = Depends(deps.get_session)):
    db_conf = session.get(Conference, conf_id)
    if not db_conf:
        raise HTTPException(status_code=404, detail="Conference not found")

    conf_data = conf.dict(exclude_unset=True)
    for key, value in conf_data.items():
        setattr(db_conf, key, value)

    session.add(db_conf)
    session.commit()
    session.refresh(db_conf)

    return db_conf
