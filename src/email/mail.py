from socket import gaierror
import smtplib


sender = "Luis Mizuno <pythonapplmd@gmail.com>"
receiver = "Luis Mizuno<pythonapplmd@gmail.com>"
login = "pythonapplmd@gmail.com"
password = """n>7`C45B_x{>(9K6"""


def mailError():
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    try:
        with conn as server:
            server.starttls()
            server.login(login, password)
            server.sendmail(sender, receiver, 'Error at your script, go checkit')
            server.quit()
    except (gaierror, ConnectionRefusedError):
        # tell the script to report if your message was sent or which errors need to be fixed
        print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
    else:
        print('Sent successfully!!!!!')


def emailUpdate(messages):
    conn = smtplib.SMTP("smtp.gmail.com", 587)
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
            print('Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))
        else:
            print('Sent successfully!!!!!')