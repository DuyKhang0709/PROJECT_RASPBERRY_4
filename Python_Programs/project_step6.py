from flask import Flask
import os

CAMERA_FOLDER_PATH = "/home/duykhang0709/camera"
LOG_FILE_NAME = CAMERA_FOLDER_PATH + "/photo_logs.txt"
photo_counter = 0

app = Flask(__name__, static_url_path=CAMERA_FOLDER_PATH, static_folder=CAMERA_FOLDER_PATH)

@app.route("/")
def index():
    return "Hello"

@app.route("/check-movement")
def check_movement():
    message = ""
    line_counter = 0
    last_photo_file_name = ""
    if os.path.exists(LOG_FILE_NAME):
        with open(LOG_FILE_NAME, "r") as f:
            for line in f:
                line_counter += 1
                last_photo_file_name = line
        global photo_counter
        difference = line_counter - photo_counter
        message = str(difference) + " photos were taken since you last checked. <br/><br/>"
        message += "Last photo: " + last_photo_file_name + "<br/>"
        message += "<img src=\"" + last_photo_file_name + "\">"
        photo_counter = line_counter
    else:
        message = "Nothing new"
    return message
        
app.run(host="0.0.0.0")