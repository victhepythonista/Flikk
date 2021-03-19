### FLikk is an easy to use webscrapper ,
#  [ I also have many versions of these scripts  I'll be uploading]
### with an easy to use interface  and  also has a 
## GUI coming too !



# WARNING
#  consequences that arise from illegal use of this software are 
# all on the user user

from settingsconfig  import SettingsConfig  as SC
from scrapper import WebsiteScrapper1
from sprkl import Sprkl
import time


from logger import Logger
s  = Sprkl()

dur = 1
disconnect_message = s.ntf("""
    __________________________
    ERROR MESSAGE TRY  TO:
    ---------------
    
    # check your network
    # disable firewall
    # check fo errors in the code 
    # check the try stements properlyhek
    #  """)

help_info = """
        ___________________________________
        WELCOME Flikks Interactive Terminal
        -----------------------------------
        scrap       [ scrap a single website name and saves the data]
        js          [ get javascript files and links from a website and saves the data]
        help / h    [ for help ]
        a           [ about ]





        dont worry more functionality is on its way
        

        """
intro = """
                    F L I K K 
                __________________
                    
    A web scrapper by Leting Victor Kipkemboi

    The terminal is under a major development 
    so many features are not in yet 
    and there is more to come

    I want this to be a scraper of its kind and
    if possible be the most powerful around !!!  


    press -h   for help

    Enjoy.......\n"""
about = """\n

    Flikk is a web scrapping software developed by me,

     Leting Victor Kipkemboi  
     copyright@2020

    The first scripts were more of minin-projects
    but they get more and more advanced 
    as we go on.

    This software can be extremely powerful !!
 
    I hope to get more and more contributers."""
class FlikkInterface:
    def __init__(self):
        self.scapper = None
        self.run = True
        self.scrapper = WebsiteScrapper1()


    def excecutecommand(self, command):
        stripped = command.split()        
        comm = stripped[0]
        length = len(stripped)
        if len(stripped) == 1:
            parameter = None
        elif len(stripped) > 1:
            parameter = stripped[1]
        
       
        if comm == 'scrap':
            if parameter ==  None:
                print("scrap  COMMAND needs a parameter :\n eg [scrap https//thiswebsite.com]")
            else:
                try:
                    s.ntf('initiating scrappin...one sec pleasse')
                    time.sleep(dur)
                    WebsiteScrapper1().scrap_site(parameter)
                except:
                    
                    pass

        elif comm == 'js':
            if parameter == None:
                s.ntf("js COMMAND needs a parameter \n eg . [js https//:mwwebsitename.co.ke]")
            else:
                print("\ngetting JAVASCRIPT from ", parameter)
                time.sleep(dur)
                
                
                s.ntf("\ninitiating scrap.....")
                WebsiteScrapper1().scrap_javascript(parameter)
    #        except:
#               s.ntf(disconnect_message)
        
        elif comm == 'a':
            print(about)
        
        elif comm == 'h' or comm == 'help':
            print(help_info)

        elif comm == 'quit' :
            s.ntf("exiting the terminal")
            self.run = False

    def Terminal(self):
       
        while self.run == True:
            choice = input(" >>| ")
            if choice == "":
                pass
            else:
                self.excecutecommand(choice)
            
    def UserInterface(self):
        print(intro)
        self.Terminal()


        
FlikkInterface().UserInterface()