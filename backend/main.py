from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoginData(BaseModel):
    username: str
    password: str

# Dummy user data for demonstration
users = {
    "exampleUser": "examplePassword"
}

@app.post("/login")
async def login(data: LoginData):
    username = data.username
    password = data.password
    
    if username in users and users[username] == password:
        return {"status": "success", "message": "Login successful!"}
    else:
        return {"status": "failed", "message": "Login failed!"}
