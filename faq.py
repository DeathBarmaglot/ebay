import webbrowser
import requests, keyboard 
from bs4 import BeautifulSoup

#from msvcrt import getch

    
cars=[]
a=[]
k=1
URL='' # 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=Behringer+x'
while True:

    HOST = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=Behringer+x'
    URL=HOST+'&_pgn='+str(k)
    HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
               'accept': '*/*'}

    def get_html(URL, params=None):
       return requests.get(URL, headers=HEADERS, params =params)

       

    def get_content(html):
        soup= BeautifulSoup(html, 'html.parser')
        items = soup.find_all('li', class_='s-item')
        

        
        for i in items:
            cars.append({
                #'div': i.find('img', class_='fleft'),
                #'title': i.find('div', class_='space rel').get_text(strip=True),
                'zaq': i.find('h3', class_='s-item__title'),
##                    'link': i.find('a', class_='s-item__link').get('href'),
                'price': i.find('span', class_='s-item__price'),
                })
    #print (cars)
            
            #break
            
    ##        
    ##
    ##            if isinstance(b, str):
    ##                
    ##                print(b)
    ##                #webbrowser.open(b, new=0)
    ##                
    ##            else: pass
    #                #print(b.text)
    ##                
    ##            #
    ##        break
    ##       #print(c, type(c))
    ##            #print(k, type(k))
    ##       
    ##
    ##           
    ##       

    def parse():
        html = get_html(URL)
        if (html.status_code) == 200:
            
            print(get_content(html.text))
            
        else: print('error')

    parse()
    k+=1
    
    for c in cars:
        for b in c.values():
            if b is not None:
                print(b.text)
                
##            break
##            print((b))
    print(URL)
    if keyboard.is_pressed(' '): 
        break
        if keyboard.is_pressed(' '): resume
    

    #break
