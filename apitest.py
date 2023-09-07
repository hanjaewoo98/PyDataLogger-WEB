import datetime

import requests
import json

url = "http://obdlogger.site:8000/api/drivedata/1"
# url = "http://localhost:8000/api/drivedata/1"
data = {
        "loggedUser": "admin",
        "datetime": str(datetime.datetime),
        "avgSpeed": "111",
        "maxSpeed": "101",
        "avgRPM": "4111",
        "maxRPM": "6124",
        "avgThrottlePos": "50",
        "avgEngineLoad": "50",
        "avgCoolantTemp": "54",
        "avgIntakeTemp": "51",
        "avgDriveTime": "52"
    }

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    data = response.json()
    # Process the response data
    print(data)
else:
    print("Request failed with status code:", response.status_code, response.reason)
