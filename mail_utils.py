from flask_mail import Mail, Message

mail = Mail()

def send_contact_email(full_name, email, phone_number, subject, budget, message):
    try:
        msg = Message(
            subject=f"New inquery from portfolio app: {subject}",
            sender='wtfnoob.who@gmail.com',
            recipients=['sohun.me@gmail.com']
        )
        msg.body = f"""
        Full Name: {full_name}
        Email: {email}
        Phone Number: {phone_number}
        Subject: {subject}
        Budget: {budget}
        Message: {message}
        """
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False