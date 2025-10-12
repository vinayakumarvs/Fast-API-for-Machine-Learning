import logging
from fastapi import FastAPI

app = FastAPI()

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] (line:%(lineno)d) %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

@app.get("/debug")
def debug_route():
    logging.info("This is an info log")
    logging.info("Another info log")
    return {"message": "Check the logs for debug information"}
