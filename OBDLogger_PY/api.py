from fastapi import FastAPI
from pydantic import BaseModel
import pynecone as pc
from OBDLogger_PY.base_state import StoreApiDataModel, DriveData, SpeedData, RPMData, TempData, DriveTimeData

app = FastAPI()


class StoreApiData(BaseModel):
    loggedUser: str
    datetime: str
    driveDataType: str
    driveData: str


class ApiDto(BaseModel):
    loggedUser: str
    datetime: str
    avgSpeed: str
    maxSpeed: str
    avgRPM: str
    maxRPM: str
    avgThrottlePos: str
    avgEngineLoad: str
    avgCoolantTemp: str
    avgIntakeTemp: str
    avgDriveTime: str


@app.get("/api/status")
async def return_sttus():
    return {"status": "OK"}


@app.post("/api/drivedata/{user_id}")
async def api_store_drivedata(user_id: str, item: ApiDto):
    loggeduser = item.loggedUser
    datetime = item.datetime
    avgspeed = item.avgSpeed
    maxspeed = item.maxSpeed
    avgrpm = item.avgRPM
    maxrpm = item.maxRPM
    avgthrottlepos = item.avgThrottlePos
    avgengineload = item.avgEngineLoad
    avgcoolanttemp = item.avgCoolantTemp
    avgintaketemp = item.avgIntakeTemp
    avgdrivetime = item.avgDriveTime

    with pc.session() as session:
        session.add(DriveData(loggedUser=loggeduser, datetime=datetime, avgSpeed=avgspeed, maxSpeed=maxspeed,
                              avgRPM=avgrpm, maxRPM=maxrpm, avgThrottlePos=avgthrottlepos, avgEngineLoad=avgengineload,
                              avgCoolantTemp=avgcoolanttemp, avgIntakeTemp=avgintaketemp, avgDriveTime=avgdrivetime))
        session.add(SpeedData(loggedUser=loggeduser, datetime=datetime, avgSpeed=avgspeed, maxSpeed=maxspeed))
        session.add(RPMData(loggedUser=loggeduser, datetime=datetime, avgRPM=avgrpm, maxRPM=maxrpm))
        session.add(TempData(loggedUser=loggeduser, datetime=datetime, avgCoolantTemp=avgcoolanttemp,
                             avgIntakeTemp=avgintaketemp))
        session.add(DriveTimeData(loggedUser=loggeduser, datetime=datetime, avgDriveTime=avgdrivetime))

        session.commit()

    return {"postId": user_id, "status": "Data stored successfully"}

# @app.post("/api/store/{item_id}")
# async def api_store_data(item_id: int, item: StoreApiData):
#     loggedUser = item.loggedUser
#     datetime = item.datetime
#     driveDataType = item.driveDataType
#     driveData = item.driveData
#     with pc.session() as session:
#         session.add(StoreApiDataModel(loggedUser=loggedUser, datetime=datetime, driveDataType=driveDataType,
#                                       driveData=driveData))
#         session.commit()
#     return {"postId": item_id, "status": "OK"}
