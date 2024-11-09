from sqlalchemy.orm import Session
from models import Meal, UserPreferences, MealPlan

# Add a new meal
def add_meal(db: Session, name: str, calories: float, protein: float, carbs: float, fat: float):
    meal = Meal(name=name, calories=calories, protein=protein, carbs=carbs, fat=fat)
    db.add(meal)
    db.commit()
    db.refresh(meal)
    return meal

# Remove a meal by ID
def remove_meal(db: Session, meal_id: int):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if meal:
        db.delete(meal)
        db.commit()
    return meal

# Get user preferences
def get_user_preferences(db: Session, user_id: int):
    return db.query(UserPreferences).filter(UserPreferences.user_id == user_id).first()

# Create a new meal plan entry
def create_meal_plan(db: Session, user_id: int, day: str, meal_id: int):
    meal_plan = MealPlan(user_id=user_id, day=day, meal_id=meal_id)
    db.add(meal_plan)
    db.commit()
    db.refresh(meal_plan)
    return meal_plan