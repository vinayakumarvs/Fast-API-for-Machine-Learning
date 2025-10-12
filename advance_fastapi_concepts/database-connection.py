from fastapi import FastAPI, Depends

app = FastAPI()

# Dependency Function to simulate a database connection
def get_db():
    db = {"connection": "Database connection established"}
    try:
        yield db
    finally:
        db.close()


# Endpoint that uses the database connection
@app.get("/home")
async def read_home(db=Depends(get_db)):
    return {'db_status': db['connection'], 'message': 'Welcome to the home page!'}

