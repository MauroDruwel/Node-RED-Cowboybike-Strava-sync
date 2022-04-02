import requests
import json
import sys
import os

json = json.loads(sys.argv[1])
files = {
                "file": (
                    json["filename"],
                    open(json["filename"], "rb"),
                    "application-type",
                )
        }
payload = {
                "activity_type": "ebikeride",
                "name": json["title"],
                "data_type": "tcx",
                "description": f"Average motor power: {json['average_motor_power']}W\nAverage user power: {json['average_user_power']}W",
}
req = requests.post(
                        "https://www.strava.com/api/v3/uploads",
                        headers={"Authorization": f"Bearer {json['access_token']}"},
                        data=payload,
                        files=files,
                    )
os.remove(json["filename"])