import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = ""
receiver_email = ""
passwd = ""
message = """\
Subject: ALERT!

Some Intruder Motion has been Detected!."""

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
	server.ehlo()  # Can be omitted
	server.starttls(context=context)
	server.ehlo()  # Can be omitted
	server.login(sender_email, passwd)
	server.sendmail(sender_email, receiver_email, message)

