from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


DATABASE_URL = "postgresql://postgres:7D129852@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Meals Table
class Meal(Base):
    __tablename__ = 'meals'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    calories = Column(Float, nullable=False)
    protein = Column(Float, nullable=False)
    carbs = Column(Float, nullable=False)
    fat = Column(Float, nullable=False)

# User Preferences Table
class UserPreferences(Base):
    __tablename__ = 'user_preferences'
    id = Column(Integer, primary_key=True, index=True)
    daily_calories = Column(Float, nullable=False)
    daily_protein = Column(Float, nullable=False)
    daily_carbs = Column(Float, nullable=False)
    daily_fat = Column(Float, nullable=False)
    meals_per_day = Column(Integer, nullable=False)

# Meal Plans Table
class MealPlan(Base):
    __tablename__ = 'meal_plans'
    id = Column(Integer, primary_key=True, index=True)
    day = Column(String, nullable=False)
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    meal = relationship("Meal")

# Create tables in the database
Base.metadata.create_all(bind=engine)