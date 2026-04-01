from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.habit import Habit as HabitModel
from app.schemas.habit import HabitCreate, Habit
from app.db import SessionLocal, get_db

router = APIRouter(prefix="/habits", tags=["habits"])

@router.post("/", response_model=Habit)
def create_habit(habit: HabitCreate, db: Session = Depends(get_db)) -> Habit:
    db_habit = HabitModel(
        name=habit.name,
        occurance=habit.occurance,
        frequency=habit.frequency,
        habit_type=habit.habit_type,
        target_value=habit.target_value,
        description=habit.description,
        is_active=habit.is_active,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

@router.get("/", response_model=list[Habit])
def read_habits(db: Session = Depends(get_db)) -> list[Habit]:
    habits = db.query(HabitModel).all()
    return habits

@router.get("/{habit_id}", response_model=Habit)
def read_habit(habit_id: int, db: Session = Depends(get_db)) -> Habit:
    habit = db.query(HabitModel).filter(HabitModel.id == habit_id).first()
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit

# Placeholder for update endpoint
# @router.put("/{habit_id}", response_model=schemas.Habit)
# def update_habit(habit_id: int, habit: schemas.HabitCreate, db: Session = Depends(get_db)):
#     pass

# Placeholder for delete endpoint
# @router.delete("/{habit_id}")
# def delete_habit(habit_id: int, db: Session = Depends(get_db)):
#     pass

# Placeholder for mark_as_done endpoint
# @router.post("/{habit_id}/done")
# def mark_habit_as_done(habit_id: int, db: Session = Depends(get_db)):
#     pass</content>

