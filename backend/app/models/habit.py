import enum

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum

from app.db import Base
from app.constants import Occurance, HabitType



class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    occurance = Column(Enum(Occurance), nullable=False)
    frequency = Column(Integer, nullable=False)
    habit_type = Column(Enum(HabitType), nullable=False, index=True)
    target_value = Column(Integer, nullable=True) # only used for numeric or duration habits, can be null for binary habits
    description = Column(String, index=True, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class HabitEntry(Base):
    __tablename__ = "habit_entries"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"))
    date = Column(DateTime)
    is_completed = Column(Boolean, default=False)
    value = Column(Integer, nullable=True) # only used for numeric or duration habits, can be null for binary habits
    note = Column(String, nullable=True)