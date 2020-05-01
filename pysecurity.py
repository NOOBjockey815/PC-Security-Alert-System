import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

#To click picture using openCV
camera = cv2.VideoCapture(0)
for i in range(1):
    return_value, image = camera.read()
    cv2.imwrite('opencv.png', image)
del(camera)

#To send the attachment through mail.

fro = "Sender's Mail"
to = "Receiver's Mail"

data = MIMEMultipart()
data['From'] = fro
data['To'] = to
data['Subject'] = "Intruder Alert!"

filename = "opencv.png"
attachment = open("opencv.png", "rb")

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

data.attach(p)

s = smtplib.SMTP('smtp.gmail.com', 587) #For Gmail accounts

s.starttls()
s.login(fro, "Email's Password")

text = data.as_string()

s.sendmail(fro, to, text)
s.quit()

#To delete the picture from the computer

os.remove("opencv.png")
print("File Removed!")