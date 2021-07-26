import requests
from bs4 import BeautifulSoup
import pandas as pd

prop_list = []

def extract(url, pag):

    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',    
        'referer' : 'https://www.zillow.com/manhattan-new-york-ny/rentals/%s_p' % (pag),
    }

    print('https://www.zillow.com/manhattan-new-york-ny/rentals/%s_p' % (pag))

    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    Props = soup.find_all('div', class_ = 'list-card-info')

    return Props

def transform(props):

    for prop in props:
        try:
            addres = prop.find('address', class_ = 'list-card-addr').text
        except:
            addres = "-"
        try:
            price = prop.find('div', class_ = 'list-card-price').text
        except:
            price = "-"
        
        try:
            details = prop.find('ul', class_ = 'list-card-details').text
        except:
            details = "-"


        PROP = {

            'Address' : addres,
            'Price' : price,
            'Details' : details,
        }

        prop_list.append(PROP)

        print(addres)
        print(price)
        print(details)

        print("""
        
        """)

for i in range(1,11):

    print('https://www.zillow.com/homes/for_rent/Manhattan,-New-York,-NY_rb/%s_p' % i)
    
    props = extract('https://www.zillow.com/homes/for_rent/Manhattan,-New-York,-NY_rb/%s_p' % i, i)
    transform(props)

def load(list):

    df = pd.DataFrame(list, columns= ["Address", "Price", "Details"])
    df.to_excel('Properties_Manhatan_NY.xls', index= False, columns= ["Address", "Price", "Details"])

load(prop_list)