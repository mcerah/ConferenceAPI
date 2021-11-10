from typing import Optional, List

from sqlmodel import Field,  SQLModel, Relationship
from app.models.talk import Talk, SpeakerTalkLink, ParticipantTalkLink


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_name: str
    mail: str
    talks_as_speaker: List["Talk"] = Relationship(
        back_populates="speakers", link_model=SpeakerTalkLink)
    talks_as_participant: List["Talk"] = Relationship(
        back_populates="participants", link_model=ParticipantTalkLink)

# class Speaker(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     person_id: int = Field(foreign_key="person.id")
#     talks: List["Talk"] = Relationship(
#         back_populates="speakers", link_model=SpeakerTalkLink)


# class Participant(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     person_id: int = Field(foreign_key="person.id")
#     talks: List["Talk"] = Relationship(
#         back_populates="participants", link_model=ParticipantTalkLink)
