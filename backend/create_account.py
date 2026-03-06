from fastapi import APIRouter  
from database import SessionLocal, User
route = APIRouter()
@route.post("/create_user")
async def Create_User(json: dict):
    email = json.get("email").strip()
    password = json.get("password").strip()
    if not email or not password:
        return {"message": "Email and password are required.", "status_code": 400}
    elif "@" not in email:
        return {"message": "Invalid email format.", "status_code": 400}
    elif len(password) < 6:
        return {"message": "Password must be at least 6 characters long.", "status_code": 400}
    elif len(password) > 50:
        return {"message": "Password must be less than 50 characters long.", "status_code": 400}
    elif len(email) > 100:
        return {"message": "Email must be less than 100 characters long.", "status_code": 400}
    elif any(c.isspace() for c in email):
        return {"message": "Email and password cannot contain whitespace.", "status_code": 400}
    db = SessionLocal()
    try:
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            return {"message": "User with this email already exists.", "status_code": 400}
        new_user = User(email=email, password=password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": f"User with email {email} created successfully!", "status_code": 200}
    finally:
        db.close()