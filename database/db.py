from models.meal_model import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()