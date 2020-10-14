#import logging

#from locators.photo_locators import PhotoLocators

#logger = logging.getLogger('books_app.books_page')

class PhotoParser:
    """
    Given specific photo divs, get comments from the photo.
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Photo caption: "{self.caption}">'

    @property
    def caption(self): # use alt attr
        #locator = PhotoLocators.CAPTION
        caption = self.parent.attrs['alt']
        #logger.debug(f'found book: `{book_title}`')
        return caption