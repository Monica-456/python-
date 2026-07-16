import smtplib
from email.message import EmailMessage
sender_email = "ksatyamonica@gmail.com"
password = "gskrtyayumrqfpjh"
reciever_email = "mahalakshmirongala10406@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message["subject"] = "Welcome Mail"
message.set_content(f"""
Hello Mahalakshmi!

Welcome to our python class

Regards,
python Team
""")

try:
    smtp = smtplib.SMTP("smtp.gmail.com", port=587) 
    smtp.starttls()
    smtp.login(sender_email, password)
    smtp.send_message(message)
    print("Email sent sucessfully")
except Execption as e:
    print("Error: ", e)
finally:
    smtp.quit()


