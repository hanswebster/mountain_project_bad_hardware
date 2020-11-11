#deprecated as of last commit (oct 28 2020)


import 

#from locators.photo_locators import PhotoLocators

#logger = logging.getLogger('books_app.books_page')

class SubcomponentParser:
    """
    Given specific photo divs, get comments from the photo.
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Sub: "{self.link}">'

    @property
    def link(self): # use alt attr
        link = self.parent.attrs['href']
        #logger.debug(f'found book: `{book_title}`')
        return link

    @property
    def sub_page(self):
        return 