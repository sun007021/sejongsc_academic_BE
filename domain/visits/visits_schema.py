import datetime

from pydantic import BaseModel


class Visits(BaseModel):
    user_id: int
    booth_id: int
    start_time: datetime.datetime
    end_time: datetime.datetime

    class Config:
        orm_mode = True

class VisitCreate(BaseModel):
    user_id: int
    booth_id: int
    #start_time: datetime.datetime
    #end_time: datetime.datetime