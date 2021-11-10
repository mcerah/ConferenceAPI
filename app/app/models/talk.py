# from app.models.person import Person

from typing import Optional, List
from datetime import datetime

from sqlmodel import Field,  SQLModel, Relationship


class SpeakerTalkLink(SQLModel, table=True):
    person_id: Optional[int] = Field(
        default=None, foreign_key="person.id", primary_key=True
    )
    talk_id: Optional[int] = Field(
        default=None, foreign_key="talk.id", primary_key=True
    )


class ParticipantTalkLink(SQLModel, table=True):
    person_id: Optional[int] = Field(
        default=None, foreign_key="person.id", primary_key=True
    )
    talk_id: Optional[int] = Field(
        default=None, foreign_key="talk.id", primary_key=True
    )


class TalkBase(SQLModel):
    title: str
    description: str
    duration: str
    date_time: datetime
    conference_id: int = Field(foreign_key="conference.id")
    speakers: List["Person"] = Relationship(
        back_populates="talks_as_speaker", link_model=SpeakerTalkLink)
    participants: List["Person"] = Relationship(
        back_populates="talks_as_participant", link_model=ParticipantTalkLink)


class Talk(TalkBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    speakers: List["Person"] = Relationship(
        back_populates="talks_as_speaker", link_model=SpeakerTalkLink)
    participants: List["Person"] = Relationship(
        back_populates="talks_as_participant", link_model=ParticipantTalkLink)


class TalkUpdate(SQLModel):
    title: Optional[str]
    description: Optional[str]
    duration: Optional[str]
    date_time:  Optional[datetime]
    conference_id: Optional[int] = Field(
        default=None, foreign_key="conference.id")
    speakers: Optional[List[int]]
    participants: Optional[List[int]]


class TalkCreate(TalkBase):
    speakers: List[int]
    participants: List[int]
