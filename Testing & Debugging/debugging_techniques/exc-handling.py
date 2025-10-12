from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": str(exc)})


@app.get("/exception")
def exception_route():
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})