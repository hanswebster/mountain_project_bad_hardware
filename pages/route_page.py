from bs4 import BeautifulSoup

from locators.route_page_locators import RoutePagePrinterLocators
from parsers.photo import PhotoParser
from parsers.comment import CommentParser

#logger = logging.getLogger('books_app.books_page')

class RoutePage:
    def __init__(self, page): #takes in entire html page from requests
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def description(self):
        locator = RoutePagePrinterLocators.DESCRIPTION
        description_tag = self.soup.select(locator)[0]
        #print(description_tag.get_text())
        return description_tag.get_text()

    @property
    def protection(self):
        locator = RoutePagePrinterLocators.PROTECTION
        protection_tag = self.soup.select(locator)[2]
        #print(protection_tag.get_text())
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