from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/", StaticFiles(directory=os.path.dirname(os.path.abspath(__file__)), html=True), name="static")
