from socket import gaierror
import smtplib
import json
import os
import time
mailInfo = {}

# path = os.path.join(os.getcwd(), '..', '..', 'user_info.json')
# path = "C:\\Python\\mailmeBot\\user_info.json"

# path = os.path.join('..', '..', 'user_info.json')
# path = os.path.abspath('user_info.json')
rel_path = """./../../user_info.json"""
script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0]
# ^-- absolute dir the script is in
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as f:
    mailInfo = json.loads(f.read())


sender = mailInfo['sender-name'] + ' <' + mailInfo['email-login'] + '>'
receiver = mailInfo['receiver-email']
login = mailInfo['email-login']
password = mailInfo['email-password']
smtp_server_address = mailInfo['smtp-server-address']
smtp_TLS_port = mailInfo['smtp-tls-port']


def mailError():
    localtime = time.asctime(time.localtime(time.time()))
    conn = smtplib.SMTP(smtp_server_address, smtp_TLS_port)
    try:
        with conn as server:
            server.starttls()
            server.login(login, password)
            server.sendmail(sender, receiver, 'Error at your script, go checkit')
            server.quit()
    except (gaierror, ConnectionRefusedError):
        # tell the script to report if your message was sent or which errors need to be fixed
        print(localtime, ': Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print(localtime, ': Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print(localtime, ': SMTP error occurred: ' + str(e))
    else:
        print(localtime, ': Sent successfully!!!!!')


def emailUpdate(messages):
    conn = smtplib.SMTP(smtp_server_address, smtp_TLS_port)
    localtime = time.asctime(time.localtime(time.time()))
    for m in messages:
        date = str(m['date'])
        text = str(m['data'])
        message = f"""Subject: OINP {date}!!!\n
        To: {receiver}\n
        From: {sender}\n


        New OINP UPDATE!
        \u2013    
        {text}"""

        try:
            with conn as server:
                server.starttls()
                server.login(login, password)
                server.sendmail(sender, receiver, message.encode('utf-8'))
                server.quit()
        except (gaierror, ConnectionRefusedError):
            # tell the script to report if your message was sent or which errors need to be fixed
            print(localtime, ': Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected:
            print(localtime, ': Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as e:
            print(localtime, ': SMTP error occurred: ' + str(e))
        else:
            print(localtime, ': Sent successfully!!!!!')