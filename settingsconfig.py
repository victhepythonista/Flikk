import configparser,os


class SettingsConfig():
    def __init__(self):
        self.messages = 'data/messages.ms'
        self.jsdb =  'data/js/links.scrap'

        self.message_parser = configparser.ConfigParser()
        self.message_parser.read(self.messages)
    def checkfile(self,file):
        try:
            with open(file, 'r') as f:
            
                f.close()
                return True
        except:
            with open(file, 'w') as f:
                f.close()
    def message(self, name):
        # message
        self.checkfile(self.messages)
        return self.message_parser['messages'][name]
        pass
