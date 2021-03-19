import configparser 
from settingsconfig import SettingsConfig as SC
from logger import Logger
class AppConfig:
    def __init__(self):
        self.js_database = SC().jsdb
        self.js_parser = configparser.ConfigParser()
        self.js_parser.read(self.js_database)

    
    
    def readfile(self, filename):
        self.checkfile(filename)
        with open(filename , 'r') as f:
            
            data = f.read()
            f.close()
            return data
    
    def update(self, parser):
        
        file =None
        if parser == 'js':
            parsr = self.js_parser
            file = self.js_database
            self.checkfile(file)
            with open(self.js_database, 'w') as f:
                parsr.write(f)
                f.close()



    def checkfile(self,file):
        try:
            with open(file, 'r') as f:
            
                f.close()
                return True
        except:
            with open(file, 'w') as f:
                f.close()

                ############## SCRAP FUNCTIONS  #############
    def  new_data(self,parser, website,  jslist):
        if parser == 'js':
            parser = self.js_parser
        else:
            print("PARSER NOT FOUND")
        dic = {}
        for itm in jslist:
            try:
                dic[jslist.index(itm)] = itm
              
            except:
                print("invalid  data in ", itm)
 
        print(dic)
        parser[website] = dic
        self.update('js')
    

    
