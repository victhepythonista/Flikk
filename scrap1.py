
import  random
import os
import  bs4 , requests
url = 'https://zds.zetech.ac.ke'
javasc1 = 'https://zds.zetech.ac.ke/lib/javascript.php/1599567138/blocks/mb2slider/scripts/mb2slider.js'

def remove(ext):
    list = os.listdir()
    print(list)
    for file in list:
        if file[-3::] == ext:
            print(file)
            os.remove(file)
            print('removing    .._____')
        pass
def add_crawl_data(data  , name):
    #########this function adds  data  to a file

    file  = name

    file_to_add_data  = open(file , 'w')
    file_to_add_data.write(data)
    file_to_add_data.close()
    print(name + 'has  been  created' )

def get_data_from_site(link  ,create_file):
    #$$$$$$$$$$ this gets  the html file on a single web page and returns the data  and adds it to a file

    req = requests.get(link)

    soup = bs4.BeautifulSoup(req.content, 'html.parser')

    data = soup.prettify()
    if create_file == True  or create_file is None:

        add_crawl_data(data  , str(random.randrange(2,100)))

    print(data)
    return data

js1 = 'https://zds.zetech.ac.ke/lib/javascript.php/1599567138/lib/babel-polyfill/polyfill.min.js'


def get_multi_url(urls):
    # ------this  function  gets  html files  from a ist of urls. and returns a list  of the files...lit!!!!!
    list_of_htmls = []
    for url in urls:
        file = get_data_from_site(url , True)
        print('succesfully   captured'+  '  ' +  url)
        list_of_htmls.append(file)

    return list_of_htmls
    pass

zetech_js_list = ['https://zds.zetech.ac.ke/lib/javascript.php/1599567138/lib/babel-polyfill/polyfill.min.js' ,
                  "https://zds.zetech.ac.ke/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js",
"https://zds.zetech.ac.ke/theme/jquery.php/core/jquery-3.4.1.min.js",
"https://zds.zetech.ac.ke/lib/javascript.php/1599567138/lib/javascript-static.js",
"https://text/javascript"
                  ]
def  find_element(element , data):
    #########THis   function gets  all  text  from tags in a  html doc
    ####   ____ and  returns  a string containing them
    html_text   =  bs4.BeautifulSoup(data , 'html.parser')

    all_of_it  =  html_text.find_all(element )
    print(all_of_it)
    all_text  =  []
    for tag  in  all_of_it:
        text =  tag.get_text()

        all_text.append(text)


    return  all_text

def add_data(extenson):
    pass
def go_here_get_me_element(element  , link ,filetosave ):


    req = requests.get(link)

    soup = bs4.BeautifulSoup(req.content, 'html.parser')



    contents= soup.prettify()



    element_text  = find_element(element , contents)
    name = (element + str(random.randrange(2,1000)))
    element_file  =  open(name , 'w')
    element_file.write(str(element_text))
    element_file.close()
    print('file written  ,     all DONE..............')


    return

zds  = 'https://zds.zetech.ac.ke'
portal  =  'https://online.zetech.ac.ke'

newzds = 'https://zds.zetech.ac.ke/'
#go_here_get_me_element('a' , 'https://zds.zetech.ac.ke')
def read_file(filename):
    data  = open(filename , 'r')
    return data.read()
    pass

def get_element_and_attr(url , element , attr):
    #__________gets data fro a site  and  returns  the attribute requested  from the elements requested
    #___________________________________
    data  = get_data_from_site(url , False)
    print(data)

    soup = bs4.BeautifulSoup(data , 'html.parser')


    all_elements = soup.find_all(element)
    strscript =''
    for element  in all_elements:
        attr_text = element.get(attr)
        print(attr_text)
        if attr_text is None:
            ####   getting  inline sript
            print('getting  alternative.....................')

            pass
        else:

            strscript = strscript+ '\n' + attr_text
            print('captureed         '  ,attr_text )

    return  strscript



    pass
local_host_zds = 'http://localhost:63342/sockconn/file207.html'

def  get_scripts_text(file_name  ):
    # ----------THis  funtions  reads  a  file contaning  links  and  stores the data  from
    #_____________THE  URL  IN TXT FILES

    the_data = open(file_name , 'r')
    line = 1
    count = 0

    line_by_line = the_data.readlines()
    print(line_by_line)
    for line in line_by_line:


        line.rstrip('\n')
        if line is None:
            continue
        try:

            link = requests.get(line)
            txt = link.content.decode('utf-8')
            print(txt)


            add_crawl_data(str(txt), (str(random.randrange(1, 1002)) + '.js'))
            print('adding   script  to  file .................')


            count+=1
            print('looooping')
        except:
            print('other line..........................................................................')



#remove('.js')