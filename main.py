from database.db import SessionLocal
from services.meal_selection import generate_daily_meal_plan
from crud.meal_crud import add_meal
from crud.meal_crud import set_user_preferences


# Example code to add a meal and generate a daily meal plan
def main():
    with SessionLocal() as db:
        # Add a sample meal
        add_meal(db, name="Grilled Chicken", calories=300, protein=30, carbs=5, fat=10)
        add_meal(db, name="Fried Chicken", calories=232, protein=32, carbs=3, fat=120)
        add_meal(db, name="IDK Chicken", calories=400, protein=5215, carbs=3213, fat=1330)

        # Set user preferences (example values)
        set_user_preferences(db, daily_calories=2000, daily_protein=150, daily_carbs=250, daily_fat=70, meals_per_day=3)

        # Generate a meal plan
        daily_meal_plan = generate_daily_meal_plan(db)
        print("Daily Meal Plan:")
        for meal in daily_meal_plan:
            print(f"{meal.name} - {meal.calories} kcal")


if __name__ == "__main__":
    main()