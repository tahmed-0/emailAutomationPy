import smtplib, ssl
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = ""
receiver_email = ""
password = ""
message = """\
Subject: Hello World
Type your message."""
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo() 
    server.starttls(context=context)
    server.ehlo() 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message) 