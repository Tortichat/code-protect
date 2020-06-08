from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import time

import uvicorn

app = FastAPI()



# Defining the data like this will allow for better code verbosity
class MeosMessage(BaseModel):
    uid : str
    sensor_id: str = None
    message_type: str = None
    message_name: str = None
    azimuth: float = 0.0
    elevation: float = 0.0
    fov: float = 0.0
    camera_type: int = 0
    time_stamp: int = 0
    processed: bool = False
    process_time: float = 0



# This is where we process our application logic - Note it must be a sync function
def process_application_logic(meos_message: MeosMessage):
    meos_message.processed = True
    process_time.processed = time.time()



@app.get("/is_alive")
async def is_alive():
    return {"alive": 1}

@app.get("/")
async def is_alive():
    # This implments / endpoint
    return {"Home": True}

@app.post("/sensor")
async def sensor(meos_message: MeosMessage):
  # here is rthe processing part
  process_application_logic(meos_message)
  return meos_message

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
    