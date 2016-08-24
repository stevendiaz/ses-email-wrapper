

class Message(object):

    def __init__(self, subject, sender, recipients):
        self.Source = sender
        self.Message = {
            'Subject': {},
            'Body': {
                'Html': {},
                'Text': {}
            }
        }
        self.Destination = {}
        self.Message['Subject']['Data'] = subject
        self.Destination['ToAddresses'] = recipients

    @property
    def html(self):
        return self.Message['Body']['Html']['Data']

    @html.setter
    def html(self, value):
        self.Message['Body']['Html']['Data'] = value

    @property
    def text(self):
        return self.Message['Body']['Text']['Data']

    @text.setter
    def text(self, value):
        self.Message['Body']['Text']['Data'] = value

    def dict(self):
        return self.__dict__
