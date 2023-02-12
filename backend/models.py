from pydantic import BaseModel


class Event(BaseModel):
    title: str
    e_description: str
    e_start_date: str
    e_end_date: str
