import smtplib
from email.mime.text import MIMEText

def send_alert_email(subject, body):
    sender_email = "mithudonrox7@gmail.com"
    receiver_email = "vamoshemang@gmail.com"
    password = "cxsc obnu svbn rkjd"  

    msg = MIMEText(body)
    msg['Subject'] = subject  
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  
            server.login(sender_email, password)  
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
            print("Alert sent successfully.")
    except Exception as e:
        print(f"Failed to send alert: {e}")