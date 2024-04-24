import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, from_email, password, smtp_server, smtp_port):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable security
        server.login(from_email, password)  # Log in to the SMTP server
        text = msg.as_string()  # Convert the message to a string
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Email details - replace placeholders with your actual details
subject = "GitHub Workflow Notification"
body = "The GitHub Actions workflow has completed successfully."
to_email = "i211232@nu.edu.pk"
from_email = "github.com"
password = "vlfw nyuf uhbs ywte"
smtp_server = "smtp.example.com"
smtp_port = 587

# Send the email
send_email(subject, body, to_email, from_email, password, smtp_server, smtp_port)
