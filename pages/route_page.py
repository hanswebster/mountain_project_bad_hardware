from bs4 import BeautifulSoup
import requests

from locators.route_page_locators import RoutePagePrinterLocators
from parsers.photo import PhotoParser
from parsers.comment import CommentParser
from text_miners import bolt_text_bad

#logger = logging.getLogger('books_app.books_page')

class RoutePage:
    def __init__(self, url): #takes in entire html page from requests
        self.url = url
        content = requests.get(url+'?print=1').content
        self.soup = BeautifulSoup(content, 'html.parser')

    @property
    def name(self):
        locator = RoutePagePrinterLocators.NAME
        name_tag = self.soup.select(locator)[0]
        return name_tag.get_text()
        
    @property
    def description(self):
        #locator = RoutePagePrinterLocators.DESCRIPTION
        description_title_tags = self.soup.find('h3', string='Description')
        description_tag = description_title_tags.find_next_sibling('div')
        return description_tag.get_text()

    @property
    def protection(self):
        #locator = RoutePagePrinterLocators.PROTECTION
        protection_title_tags = self.soup.find('h3', string='Protection')
        protection_tag = protection_title_tags.find_next_sibling('div')
        return protection_tag.get_text()

    @property
    def photo_captions(self):
        locator = RoutePagePrinterLocators.PHOTOS
        photo_tags = self.soup.select(locator)
        return [PhotoParser(e) for e in photo_tags]

    @property
    def comments(self):
        locator = RoutePagePrinterLocators.COMMENTS
        comment_tags = self.soup.select(locator)
        return [CommentParser(e) for e in comment_tags]
    
    @property
    def bad_gear(self): #return boolean (implemented) and indeces (eventually) for flagged comments and other areas
        desc_bad = bolt_text_bad(self.description)
        protec_bad = bolt_text_bad(self.protection)
        
        photo_bad = False
        for photo in self.photo_captions:
            photo_bad = photo_bad or bolt_text_bad(photo.caption)

        comment_bad = False
        for comment in self.comments:
            comment_bad = comment_bad or bolt_text_bad(comment.content)
        
        return any([desc_bad, protec_bad, photo_bad, comment_bad])

