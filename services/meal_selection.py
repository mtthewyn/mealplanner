from sqlalchemy.orm import Session
from models.meal_model import Meal
from crud.meal_crud import get_user_preferences
import random


def validate_meal(meal):
    # Ensure meal has valid calorie and macro values
    return all([meal.calories > 0, meal.protein > 0, meal.carbs > 0, meal.fat > 0])


def generate_daily_meal_plan(db: Session):
    # Get all meals from the database
    meals = db.query(Meal).all()
    meals = [meal for meal in meals if validate_meal(meal)]

    # Get user preferences
    user_preferences = get_user_preferences(db)

    # Initialize counters for daily totals
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    # List to hold selected meals for the day
    daily_meal_plan = []

    # Define the calorie tolerance (+-20)
    calorie_tolerance = 20

    while not (user_preferences.daily_calories - calorie_tolerance <= total_calories <= user_preferences.daily_calories + calorie_tolerance):
        # Randomly select a meal
        meal = random.choice(meals)

        # Add the meal to the daily plan
        daily_meal_plan.append(meal)

        # Update the daily totals
        total_calories += meal.calories
        total_protein += meal.protein
        total_carbs += meal.carbs
        total_fat += meal.fat


    return daily_meal_plan