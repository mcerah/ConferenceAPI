from typing import Optional, List
from datetime import datetime

from sqlmodel import Field,  SQLModel


class ConferenceBase(SQLModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime


class Conference(ConferenceBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ConferenceUpdate(SQLModel):
    title: Optional[str]
    description: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]


class ConferenceCreate(ConferenceBase):
    pass
