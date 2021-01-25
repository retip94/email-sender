import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import pandas as pd
from string import Template
import yaml
import logging

# noinspection PyArgumentList
logging.basicConfig(handlers=[logging.FileHandler("../log.log"), logging.StreamHandler()],
                    level=logging.INFO,
                    format='%(asctime)s |  %(levelname)s | %(message)s')

MAILING_LIST_FILE = '../mailing-list.xlsx'
LOGIN_DATA_FILE = '../login-data.yaml'

message = MIMEMultipart("alternative")

message["Subject"] = "Temat wiadomości"
MESSAGE_TEMPLATE_TEXT = Template("""\
    Hi $name, 
    Template message
    
    
    Remember to visit my site
    http://cv.retip1994.usermd.net/""")
MESSAGE_TEMPLATE_HTML = Template("""\
    <html>
      <body>
        <p>Hi $name,<br>
            <h2>Template message</h2>
           Remember to visit my site<br>
           <a href="http://cv.retip1994.usermd.net/">Piotr Piekielny</a>
        </p>
      </body>
    </html>
    """)


def main():
    login_data = get_login_data()
    message["From"] = login_data.get('email', '')
    server = init_email_server(login_data)
    if server is None:
        return
    mailing_list = pd.read_excel(MAILING_LIST_FILE, engine='openpyxl')
    for idx, row in mailing_list.iterrows():
        receiver_email = row['email']
        name = row['name']
        if not validate_email(receiver_email):
            logging.error(f'{receiver_email} is not valid')
            continue
        # Add HTML/plain-text parts to message
        # The email client will try to render the last part first
        message["To"] = receiver_email
        message.attach(MIMEText(MESSAGE_TEMPLATE_TEXT.substitute(name=name), "plain"))
        message.attach(MIMEText(MESSAGE_TEMPLATE_HTML.substitute(name=name), "html"))
        try:
            server.sendmail(login_data['email'], receiver_email, message.as_string())
            logging.info(f'message to {receiver_email} sent successfully')
        except Exception as e:
            logging.error(f'error sending file to {receiver_email}: {e}')


def init_email_server(login_data):
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(login_data['smtp_server'], login_data['port'])
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(login_data['email'], login_data['password'])
        return server
    except Exception as e:
        logging.error(f'error in initializing email server: {e}')
        return None


def validate_email(email_address):
    if pd.isnull(email_address):
        return False
    email_regex = re.compile(r"^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    return email_regex.fullmatch(email_address)


def get_login_data():
    try:
        with open(LOGIN_DATA_FILE) as file:
            login_data = yaml.full_load(file)
    except FileNotFoundError:
        print("Provide your email login data")
        login_data = {
            'email': input("email: "),
            'password': input("password: "),
            'smtp_server': input('smtp server: '),
            'port': input('port: ')
        }
        with open(LOGIN_DATA_FILE, 'w') as file:
            yaml.dump(login_data, file)
    finally:
        return login_data


if __name__ == '__main__':
    main()
