from fastapi import FastAPI
import create_account, login
app = FastAPI()
app.include_router(create_account.route)  
app.include_router(login.route)
@app.get("/")
def read_root():
    return {"message": "Hello World, FastAPI is working!"}