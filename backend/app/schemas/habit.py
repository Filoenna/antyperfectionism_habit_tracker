from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from app.constants import Occurance, HabitType

class HabitBase(BaseModel):
    name: str
    occurance: Occurance
    frequency: int
    habit_type: HabitType
    target_value: Optional[int] = None
    description: Optional[str] = None
    is_active: bool = True

class HabitCreate(HabitBase):
    pass

class Habit(HabitBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
