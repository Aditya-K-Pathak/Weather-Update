import ssl
import smtplib
import pandas as pd
import main
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

html = main.news()

msgText = MIMEText(
    '<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')

email_from = 'adityapathak2874@gmail.com'
password = '9838096273'
email_to = ['adityapathak2874@gmail.com',]


date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

email_message = MIMEMultipart()
email_message['From'] = "adityapathak2874@gmail.com"
email_message['To'] = "rekhapathak149@gmail.com"
email_message['Subject'] = f'News - {date_str}'

email_message.attach(MIMEText(html, "html"))

email_string = email_message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_from, password)
    for receiver in email_to:
        server.sendmail(email_from, receiver, email_string)

print("Mail sent Successfully1")
