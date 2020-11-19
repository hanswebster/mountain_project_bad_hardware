from bs4 import BeautifulSoup
import requests

from .route_page import RoutePage
from locators.area_page_locators import AreaPageLocators, AreaPagePrinterLocators
from parsers.photo import PhotoParser
from parsers.comment import CommentParser
#from parsers.subcomponent import SubcomponentParser

class AreaPage:
    def __init__(self, url): # page of html from requests
        self.url = url
        page = requests.get(url).content
        printer_page = requests.get(url+'?print=1').content
        self.soup = BeautifulSoup(page, 'html.parser')
        self.printer_soup = BeautifulSoup(printer_page, 'html.parser')

    @property
    def name(self):
        locator = AreaPageLocators.NAME
        name_tag = self.soup.select_one(locator)
        return name_tag.get_text()

    @property
    def sub_type(self): 
        locator = AreaPageLocators.SUBTYPE
        sub_type_tag = self.soup.select(locator)[0]
        return sub_type_tag.get_text().split()[0] # extract first word
    
    @property
    def subcomponent(self):
        if self.sub_type == 'Routes':
            locator = AreaPageLocators.SUBROUTE
            subcomponent_tags = self.soup.select(locator)
            links = [tag.attrs['href'] for tag in subcomponent_tags]
            return [RoutePage(link) for link in links] #possibly replace return a route page with just process route to DB
        else: 
            locator = AreaPageLocators.SUBAREA
            subcomponent_tags = self.soup.select(locator) #.attrs['href'] #for links
            links = [tag.attrs['href'] for tag in subcomponent_tags]
            return [AreaPage(link) for link in links]
    
    @property
    def description(self):
        #locator = AreaPagePrinterLocators.DESCRIPTION
        #description_tag = self.printer_soup.select(locator)[0]
        description_title_tags = self.soup.find('h3', string='Description')
        description_tag = description_title_tags.find_next_sibling('div')
        return description_tag.get_text()

    @property
    def comments(self):
        locator = AreaPagePrinterLocators.COMMENTS
        comment_tags = self.printer_soup.select(locator)
        return [CommentParser(e) for e in comment_tags]

    @property
    def photo_captions(self):
        locator = AreaPagePrinterLocators.PHOTOS
        photo_tags = self.printer_soup.select(locator)
        return [PhotoParser(e) for e in photo_tags]

    
