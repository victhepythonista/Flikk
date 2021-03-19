
import datetime,os

from sprkl import Sprkl

s= Sprkl()
class Logger:
    def __init__(self):
        self.logfile = 'data.logg'
        self.scraplogfile = 'scraplog.logg'
        self.jslogfile = 'jslog.logg'

    
    def log(self, data):
        date = datetime.datetime.now().strftime("%Y : %m : %d :%H :%M")
        
        try:
            prev = ""
            with open(self.logfile, 'r') as f:
                prev = f.read()
                f.close()
            with open(self.logfile, 'w') as f:
                f.write(prev + "\n\n\n\n" +date + "\n"+ data)
        except:
            try:
                with open(self.logfile, 'w') as l:
                    l.write('')
                    l.close()
            except:
                print("we cant log this data", data)
            
            
    def scraplog(self, data):
        date = datetime.datetime.now().strftime("%Y : %m : %d :%H :%M")
        
        try:
            prev = ""
            with open(self.scraplogfile, 'r') as f:
                prev = f.read()
                f.close()
            with open(self.scraplogfile, 'w') as f:
                f.write(prev + "\n\n\n\n" +date + "\n"+ data)
        except:
            try:
                with open(self.scraplogfile, 'w') as l:
                    l.write('')
                    l.close()
            except:
                print("we cant log this data")
            self.scraplog(data)
    def create(self,filename):

        if  not os.path.isfile(filename):
            with open( filename, 'w') as file:
                file.close()
            
                print('ok\n')
                pass
        print(filename, 'created')
    
    def logscripts(self,data):
        date = datetime.datetime.now().strftime("%Y : %m : %d :%H :%M")
        self.create(self.jslogfile)
        new_data = ""
        for  sc in data:
            if sc is None:pass
            else:

                
                try:
                    print(f"LOGGING           ", sc)
                    
                    try:
                        prev = ""
                        with open(self.jslogfile, 'r') as f:
                            prev = f.read()
                            f.close()
                        with open(self.jslogfile, 'w') as f:
                            f.write(prev + "\n"+ sc)
                    except:
                        print("\nwe cant log this data",sc)
            
                except:
                    s.ntf("not logged")
                    print(sc)
        data = new_data
    def logdata(self,filename,directory, data):
        this= os.getcwd()
        
        self.create(filename)
        try:
            prev = ""
            with open(filename, 'r') as f:
                prev = f.read()
                f.close()
            with open(filename, 'w') as f:
                f.write(prev + "\n"+ data)
                f.close()
        
        except:
            print("\nwe cant log data")
    

