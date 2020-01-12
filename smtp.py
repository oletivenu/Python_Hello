from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Naga Venu Babu Oleti"
message["to"] = "naga.venu@mdsuae.ae"
message["subject"] = "this is a test mail"
body = template.substitute({"name": "Waynu"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("image.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("venu.babu80@gmail.com", "VENU1234")
    smtp.send_message(message)
    print("sent...")
