import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pi_command import get_ip_address

class Emailer():
    def __init__(self, sender_email="jordikitto@gmail.com", password="kqagpbhnpgbrbkbe", receiver_email="jordikitto@gmail.com"):
        self.__sender_email = sender_email
        self.__receiver_email = receiver_email
        self.__password = password
        self.__port = 465  # For SSL
        self.__smtp_server = "smtp.gmail.com"

    def send(self, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, self.__receiver_email, message)

    def send_html(self, subject, msg_plain, msg_html):
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.__sender_email
        message["To"] = self.__receiver_email
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(msg_plain, "plain")
        part2 = MIMEText(msg_html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)
        self.send(message.as_string())

    def send_ip(self):
        """Send IP address email to reciever email"""
        ip_address = get_ip_address()
        text = """Visit """+ip_address+""" to control your PlayBot!\
            
            Kind regards,
            Your Loving PlayBot"""
        html = """\
        <html>
        <body>
            <p>Visit <a href="http://"""+ip_address+"""">"""+ip_address+"""</a> to control your PlayBot!
            <br>
            <br>
            Kind regards, <br>
            Your Loving PlayBot
            </p>
        </body>
        </html>
        """
        subject = "PlayBot Address: "+ip_address
        self.send_html(subject, text, html)