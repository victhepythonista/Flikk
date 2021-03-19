from bs4 import BeautifulSoup 
import string,os
import requests

from sprkl import Sprkl
from appconfig import AppConfig
from logger import Logger
s = Sprkl()

class WebsiteScrapper1():
    def __init__(self):
        self.unwanted = [char for char in "[}]{"]
        pass
        
   
    def readfile(self, filename):
        self.checkfile(filename)
        with open(filename , 'r') as f:
            
            data = f.read()
            f.close()
            return data

    def makesoup(self, soupname):
        s.ntf(f"making soup   with {soupname}  ........")
        link = requests.get(soupname)
        soup = BeautifulSoup(link.content, 'html.parser' )
        s.ntf("soup ready !\n")
        return soup

    def prtfy(self,soup):
        return soup.prettify()
    def make_and_prtfy(self,filename):
        #returns a string of the html code
        s = self.makesoup(filename)
        s = self.prtfy(s)
        return s

    def get_attribute(self, element, attr):
        # gets an attribute from an alement
        attribute = element.get(attr)
        return(attribute)
    
    def find_all_elements(self,websitename, element):
        # returns an list  of all elements
        elements= []
        file = websitename
        soup = self.makesoup(file)

        for elmnt in soup.find_all(element) :
            elements.append(elmnt)
        print(elements)
        return elements

    def find_all_attributes(self,elements,attr):
        # returns a list of values of all the attributes
        # of the elements provides

        values = []
        for el in elements:
            print("GETTING HREF", el)
            try:
                values.append(el.get(attr))
            except:
                pass
        
            
        print(values)
        return values


    def get_link(self, site):
        link = requests.get(site)
    def strip_link(self,link):
            allowed = string.ascii_lowercase + string.ascii_uppercase + "123456789/."
            final = ""
            for item in link :
                if item in allowed:
                    final = final + item
            return final
    def get_javascript_links(self, file_or_Link):
        ## returns and can even save  a list of
        # all javascript links to a database 
        # managed by appconfi
        js = self.find_all_elements(file_or_Link, 'script')
        jsfilelinks = []
        for ele in js:
            
            link = self.get_attribute(ele, 'src')
            link = self.strip_link(link)
            jsfilelinks.append(link)
        
        AppConfig().new_data('js', file_or_Link, jsfilelinks)

        return jsfilelinks
    def make_name(self,name, ext = '.html'):
        name  =  name.replace("//", '_')
        name = name.replace(":",'_')
        name = name.replace(".", '_')
        name = name.replace("/", "_")
        filename = name + ext
        return filename
    
    def find_all_multiple_attributes(self, elements, attr_list):
        value = []
        for el in elements:
            for attr in attr_list:
                v = el.get(attr)
                if v != None:value.append(v)
        return value

    def get_script(self,url):
        ## returns the contents of the javascript in 
        # the url provided
        get =requests.get(url)
        print('\nSCRIPT DATA OF  TYPE ',type(get))
        return get.content.decode("utf-8")
    def explore_scripts(self, listofscripts):
        ## sees whats at the end of a list of javascript
        ## links
        directory = "scrapdata/"

        try:
            if not  os.path.isdir :
                os.path.makedirs(directory)
                print("making   {directory} because it does not exist\n")
        except:
            print("could not make",  directory)
        
        for script in listofscripts:
            s.ntf(f"exploring {script}") 
            try:          
                
                name = self.make_name(script, '.js')
                self.create(name)
                data = self.get_script(script)
                print(f"obtained data from   {script}  we will add it to  {name}\ncreating file......\n")
                Logger().logdata(name, directory, data)
                print("\nsaved "+ script, "to   ",name) 
            except:
                s.ntf(f"errors exploring {script}")
    def scrap_javascript(self, website):
        print("Searching for scripts.....\nscanning website...\n")
        link =None
        elements = self.find_all_elements(website, 'script')
        attributes = self.find_all_multiple_attributes(elements,['src'])
        print('fetched scripts successfully \nsaving.........')
        Logger().logscripts(attributes)
        self.explore_scripts(attributes)

  

        

    def get_data_from_site(self,link  ):
        print('making soup with', link)
        print("LINK OF TYPE", type(link))
        print(link == "https://zds.zetech.ac.ke")
        #$$$$$$$$$$ this gets  the html file on a single web page and returns the data  and adds it to a file
        req = requests.get(link)
        soup = BeautifulSoup(req.content, 'html.parser')

        print('soup ready.........\npretttifying')
        data = soup.prettify()
        return data
    def add_crawl_data(self,data  , file):
        #########this function adds  data  to a file
        with open(file, 'w') as f:
            f.write(data)
    def logg_site(self, sitename,data):
        ## log a webpage to a file
        

        self.add_crawl_data(data, sitename)
    def create(self,filename):
        try:
            if  not os.path.isfile(filename):
                with open( filename, 'w') as file:
                    file.close()
                
                    print('ok\n')
                    pass
            print(filename, 'created')
        except:
            s.ntf(f"coould not create {filename}")

    def scrap_site(self,website):
        s.ntf('scrapping > '+ website)
        print('\n\nplease be patient...PLEASE')
        name = self.make_name(website)
        filename = name 
        self.create(filename)
        print(f'\nscrap data of {website} will be saved  to  {filename}')
        data = self.get_data_from_site(website)  
        self.add_crawl_data(data, filename)         
       
        print(data)

        #except:
         #   s.ntf("cant connect to a network or invalid website name")
zds = 'https://zds.zetech.ac.ke'
        


#WebsiteScrapper1().scrap_javascript(zds)
#WebsiteScrapper1().scrap_site(zds)
