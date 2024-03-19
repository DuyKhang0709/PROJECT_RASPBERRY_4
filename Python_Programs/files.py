import os

if os.path.exists("/home/duykhang0709/text_file"):
    print("File exists")
    os.remove("/home/duykhang0709/text_file")


# with open("/home/duykhang0709/text_file", "r") as f:
#     print(f.read())