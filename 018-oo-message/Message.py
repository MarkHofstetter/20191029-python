class Message:    
    __recipient = None
    __content = None
    
    def __init__(self):
        self.__content = None
    
    def send(self, log_message = None):
        print("Loging: sending message to", self.recipient)
        print("Content:", self.content)
    
    @property
    def recipient(self):
        return "TO: " + self.__recipient
        
    @recipient.setter
    def recipient(self, value):
        self.__recipient = value
        
    @property
    def content(self):
        return self.__content
        
    @content.setter
    def content(self, content):
        self.__content = content
    
    def __repr__(self):
        return "**** To: {:s}, Body: {:s}". \
                format(self.recipient, self.content)
    
    
class SMS(Message):    
    __content = None
    
    @staticmethod
    def at_int_dial():
        return '+43'
    
    def __init__(self):
        super(SMS, self).__init__()
        
    
    def send(self):
        super(SMS, self).send(log_message = 'SMS')
        print("sending SMS to", self.recipient)
    
    @Message.content.setter
    def content(self, content):        
        if len(content) > 5:
            print("Achtung zu lange", content)
        Message.content.fset(self, content[:5])            
        
        
    
class Email(Message):
    subject = None
    
    def send(self):
        super(Email, self).send()
        print("sending Email to", self.recipient)
