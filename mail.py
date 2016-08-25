

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

    def send_mail(self, aws_region_name, aws_access_key, aws_secret_access_key):
        ses_client = boto3.client('ses', region_name=aws_region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key)
        ses_client.send_email(**self.__dict__)
