import datetime
import hashlib
import hmac
import base64
import requests
import time
import json
import pynecone as pc
from datetime import datetime
from OBDLogger_PY.base_state import DriveData, State, DriveTimeData, RPMData, SpeedData, TempData


def return_userdata():
    """Return the user data."""
    with pc.session() as session:
        drivedata = session.exec(DriveData.select.where(DriveData.loggedUser == "admin")).first()
        rpmdata = session.exec(RPMData.select.where(RPMData.loggedUser == "admin")).first()
        speeddata = session.exec(SpeedData.select.where(SpeedData.loggedUser == "admin")).first()
        tempdata = session.exec(TempData.select.where(TempData.loggedUser == "admin")).first()

        return {
            "drivedata": drivedata,
            "rpmdata": rpmdata,
            "speeddata": speeddata,
            "tempdata": tempdata,
        }


def format_for_sms(user_data):
    """Format the user data for SMS."""

    drivetime_str = ""
    drivedata = user_data['drivedata']
    if drivedata is not None:
        drivetime_str += f"주행시간: {drivedata.avgDriveTime}분\n"

    speed_str = ""
    speeddata = user_data['speeddata']
    if speeddata is not None:
        speed_str += f"최대속도: {speeddata.maxSpeed}km/h\n"

    temp_str = ""
    tempdata = user_data['tempdata']
    if tempdata is not None:
        temp_str += f"흡기온: {tempdata.avgIntakeTemp}℃\n"

    rpm_str = ""
    rpmdata = user_data['rpmdata']
    if rpmdata is not None:
        rpm_str += f"최대RPM: {rpmdata.maxRPM}RPM\n"

    return f"{drivetime_str}{rpm_str}{speed_str}{temp_str}"


def make_signature(secret_key, uri, timestamp, access_key):
    secret_key = bytes(secret_key, 'UTF-8')
    method = "POST"
    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingkey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    return signingkey


class MessageSendState(State):
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)

    access_key = "k"  # access key id (from portal or Sub Account)
    secret_key = "k"  # secret key (from portal or Sub Account)
    url = "k"
    uri = "k"
    number = "k"
    datestr = datetime.today().strftime("%Y-%m-%d")

    def send_sms(self):
        user_data = return_userdata()
        formatted_data = format_for_sms(user_data)
        contents = str(self.datestr) + "일자 통계:\n" + formatted_data
        print(contents)
        header = {
            "Content-Type": "application/json; charset=utf-8",
            "x-ncp-apigw-timestamp": self.timestamp,
            "x-ncp-iam-access-key": self.access_key,
            "x-ncp-apigw-signature-v2": make_signature(self.secret_key, self.uri, self.timestamp, self.access_key)
        }

        data = {
            "type": "SMS",
            "from": "k",
            "content": contents,
            "subject": "SENS",
            "messages": [
                {
                    "to": self.number,
                }
            ]
        }

        requests.post(self.url + self.uri, headers=header, data=json.dumps(data))
        # if requests.status_codes == 202:
        #     return "문자가 전송되었습니다."
        # else:
        #     return "문자 전송에 실패하였습니다."


