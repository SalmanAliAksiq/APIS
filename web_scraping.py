from bs4 import BeautifulSoup
from selenium_file import *

def scraping(username):
    source = linkedinUserProfile(username).page_source
    soup = BeautifulSoup(source,'lxml')

    products_data = []
    
    img_src = soup.find('div',{'class' : 'pv-top-card--photo text-align-left pv-top-card--photo-resize'}).img['src']
    intro = soup.find('div',{'class': 'mt2 relative'})
    intro_title = intro.find('h1',{'class' : 'text-heading-xlarge inline t-24 v-align-middle break-words'})
    if intro_title and intro_title is not None:
        intro_title = intro_title.text
    intro_role = intro.find('div',{'class':'text-body-medium break-words'})
    if intro_role and intro_role is not None:
        intro_role = intro_role.text.strip()
    int_tit = soup.find('ul',{"class" : "pv-text-details__right-panel"})
    p_data = int_tit.find_all('li')
    intro_company = p_data[0].text.strip()
    intro_uni = p_data[1].text.strip()
    connections = soup.find('ul',{'class' : 'pv-top-card--list pv-top-card--list-bullet display-flex pb1'})
    c_data = connections.find('span',{'class' : 't-bold'})
    if c_data and c_data is not None:
        c_data = c_data.text

    Data = {
            "title" : intro_title,
            "role" : intro_role,
            "company" : intro_company,
            "university" : intro_uni,
            "connections" : c_data,
            "profile url" : img_src
        }
    
    products_data.append(Data)
    return products_data


