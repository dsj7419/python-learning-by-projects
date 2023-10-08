import os  # For accessing environment variables
import smtplib  # Simple Mail Transfer Protocol client session object
from email.mime.multipart import MIMEMultipart  # For constructing MIME multipart message
from email.mime.text import MIMEText  # MIME-styled text
from email.mime.base import MIMEBase  # Generic MIME base class
from email import encoders  # For encoding the attachment

def get_email_credentials():
    """
    Retrieves the email address and password from environment variables.
    
    Returns:
        str, str: Email address, Email password

    Raises:
        ValueError: If email or password is not found in environment variables.
    """
    email = os.environ.get('EMAIL_ADDRESS')
    password = os.environ.get('EMAIL_PASSWORD')
    
    if not email or not password:
        raise ValueError("Email or password not found in environment variables.")
    
    return email, password

def send_email(from_email, password, subject, body, to_email, attachment_path=None):
    """
    Sends an email with the specified subject, body, and attachments to the specified recipient.
    
    Parameters:
        from_email (str): The email address of the sender.
        password (str): The password for the sender's email account.
        subject (str): The subject of the email.
        body (str): The body text of the email.
        to_email (str): The email address of the recipient.
        attachment_path (str, optional): The file path of the attachment. Defaults to None.

    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """
    try:
        # Set up the server using Gmail's SMTP server and port
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)  
        server.starttls()  # Secure the SMTP connection
        
        # Login to the email account using the provided credentials
        server.login(from_email, password)
        
        # Construct the email message using MIMEMultipart
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach the file, if provided, and encode it to be sent via email
        if attachment_path is not None:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
                msg.attach(part)
        
        # Send the constructed message and close the server connection
        server.send_message(msg)
        server.close()
        
        print(f"Email sent successfully to {to_email}.")
        return True
    
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")
        return False
