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
    # TODO: Retrieve the email and password from environment variables.
    # HINT: Use os.environ.get to access environment variables.
    email = None
    password = None
    
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
        # TODO: Set up the server using Gmail's SMTP server and port.
        # HINT: Use smtplib.SMTP to initialize the server and specify the host and port.
        server = None  
        # TODO: Secure the SMTP connection.
        # HINT: Use starttls() method to secure the connection.
        
        # TODO: Login to the email account using the provided credentials.
        # HINT: Use login method of server to login.
        
        # Construct the email message using MIMEMultipart
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # TODO: Attach the file if provided, and encode it to be sent via email.
        # HINT: Use MIMEBase to attach and encode the file.
        if attachment_path is not None:
            # Your code here
        
        # TODO: Send the constructed message and close the server connection.
        # HINT: Use send_message and close methods of server.
        
            print(f"Email sent successfully to {to_email}.") #temporarily intented to avoid errors. this should be same indent as return. please fix once you add code.
        return True
    
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")
        return False
