from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        import time
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        print(f"Request: {request.url.path} processed in {process_time:.4f} seconds")
        response.headers["X-Process-Time"] = str(process_time)
        return response


app.add_middleware(TimerMiddleware)

@app.get("/hello")
async def hello():
    for _ in range(1000000):
        pass
    return {"message": "Hello, World!"}