import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the email server
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_email@example.com'
smtp_password = 'your_email_password'

# Create the email message
msg = MIMEMultipart()
msg['From'] = 'your_email@example.com'
msg['To'] = 'victim_email@example.com'
msg['Subject'] = 'Phishing Attack'

# Create the email body
body = '''
Dear Recipient,

This is a phishing email. Please click the link below to access your account:



If you did not request this email, please ignore it.
'''

msg.attach(MIMEText(body, 'plain'))

# Connect to the email server and send the email
 smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())