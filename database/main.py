from database import get_db
from crud import add_meal
from crud import remove_meal

# db = next(get_db())
# new_meal = add_meal(db, "Chicken Salad", 300, 30, 10, 12)
# print(f"Added Meal: {new_meal.name} with {new_meal.calories} calories.")

db = next(get_db())
deleted_meal = remove_meal(db, meal_id=2)
if deleted_meal:
    print(f"Meal '{deleted_meal.name}' has been deleted.")
else:
    print("Meal not found.")