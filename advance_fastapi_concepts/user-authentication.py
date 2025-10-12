from fastapi import FastAPI, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "vinay" and form_data.password == "password":
        return {"access_token": "fake-jwt-token", "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

def decode_token(token: str):
    if token == "fake-jwt-token":
        return {"username": "vinay"}
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

@app.get("/profile")
async def get_profile(current_user: dict = Depends(get_current_user)):
    return {"username": current_user["username"], "email": f"{current_user['username']}@example.com"}