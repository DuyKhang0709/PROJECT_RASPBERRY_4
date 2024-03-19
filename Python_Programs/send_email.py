import yagmail


password = ""

with open("/home/duykhang0709/.local/share/.email_password", "r") as f:
    password = f.read()
    
    
yag = yagmail.SMTP('duykhang0709raspberry@gmail.com', password)

yag.send(to='ankhangtn2003s@gmail.com',
         subject="first email",
         contents="Hello from Raspberry Pi",
         attachments="/home/duykhang0709/2024-03-13-204356_1920x1080_scrot.png")

print("Email sent")

#quang.nguyen2005@hcmut.edu.vn