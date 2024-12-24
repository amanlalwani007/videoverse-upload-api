from dotenv import load_dotenv

load_dotenv()
# to run  in local run .env


import logging

from config import config
from database import Base, engine
from fastapi import FastAPI
from routers import download, merge, share, trim, upload

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(upload.router)
app.include_router(trim.router)
app.include_router(merge.router)
app.include_router(share.router)
app.include_router(download.router)

import uvicorn

if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    logging.info("stating the server")
    uvicorn.run("main:app", host="0.0.0.0", port=config.PORT, reload=True)
