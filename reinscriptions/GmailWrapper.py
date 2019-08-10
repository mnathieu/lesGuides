import smtplib


class GmailWrapper:
    def connectToSMTP(self):
        self.server.connect('smtp.gmail.com', 587)  # for eg. host = 'smtp.gmail.com', port = 587
        self.server.ehlo()
        self.server.starttls()
        try:
            self.server.login(self.userName, self.pswrd)
        except (smtplib.SMTPAuthenticationError):
            print 'Utilisateur ' + self.userName + ' ou mot de passe ' + self.pswrd + ' incorrect. S ils sont correct veuillez autoriser l acces aux applications moins securisees sur votre compte google https://www.google.com/settings/security/lesssecureapps'
            raise

    def __init__(self, _user, _pswrd):
        self.userName = _user
        self.mailAddress = _user + '@gmail.com'
        self.pswrd = _pswrd
        self.server = smtplib.SMTP()
        self.connectToSMTP()

    def __del__(self):
        self.closeServer()

    def sendEmail(self, mailTo, mimeContent):
        if (mailTo is 'EMail') or (not mailTo) or (mailTo is 'mail@mail.com'):
            print('Invalid email early detection')
            raise
        try:
            self.server.sendmail(self.mailAddress, mailTo, mimeContent.as_string())
        except (smtplib.SMTPRecipientsRefused):
            print('Enter SMTPRecipientsRefused')
            raise
        except (smtplib.SMTPServerDisconnected):
            # Timeout on the server. Re init the connection + try again
            print('Enter SMTPServerDisconnected Trying to re-connect')
            try:
                self.closeServer()
            except:
                pass
            self.connectToSMTP()
            self.server.sendmail(self.mailAddress, mailTo, mimeContent.as_string())
        except:
            print('Enter Exception')
            self.closeServer()
            self.connectToSMTP()
            raise

    def closeServer(self):
        self.server.quit()

