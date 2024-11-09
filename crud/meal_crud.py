from sqlalchemy.orm import Session
from models.meal_model import *

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
def get_user_preferences(db: Session):
    return db.query(UserPreferences).first()  # Fetches the first entry in the table


# Add or update user preferences
def set_user_preferences(db: Session, daily_calories: float, daily_protein: float,
                         daily_carbs: float, daily_fat: float, meals_per_day: int):
    # Check if preferences already exist
    user_preferences = db.query(UserPreferences).first()

    if user_preferences:
        # Update existing preferences
        user_preferences.daily_calories = daily_calories
        user_preferences.daily_protein = daily_protein
        user_preferences.daily_carbs = daily_carbs
        user_preferences.daily_fat = daily_fat
        user_preferences.meals_per_day = meals_per_day
    else:
        # Create new user preferences
        user_preferences = UserPreferences(
            daily_calories=daily_calories,
            daily_protein=daily_protein,
            daily_carbs=daily_carbs,
            daily_fat=daily_fat,
            meals_per_day=meals_per_day
        )
        db.add(user_preferences)

    db.commit()
    db.refresh(user_preferences)
    return user_preferences

# Create a new meal plan entry
def create_meal_plan(db: Session, day: str, meal_id: int):
    meal_plan = MealPlan(day=day, meal_id=meal_id)
    db.add(meal_plan)
    db.commit()
    db.refresh(meal_plan)
    return meal_plan

# Clear existing meal plan entries for a fresh start each week/day
def clear_meal_plan(db: Session):
    db.query(MealPlan).delete()
    db.commit()