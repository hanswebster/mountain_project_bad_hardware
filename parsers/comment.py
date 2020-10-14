#import logging

from locators.comment_locators import CommentLocators

#logger = logging.getLogger('books_app.books_page')

class CommentParser:
    """
    Given specific photo divs, get comments from the photo.
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Comment: "{self.content}", made on {self.date}>'

    @property
    def content(self): 
        locator = CommentLocators.CONTENT
        content = self.parent.get_text()
        content = content[55:-55:]
        content = content
        #logger.debug(f'found book: `{book_title}`')
        return content

    @property
    def date(self): 
        locator = CommentLocators.DATE
        date = self.parent.select_one(locator).get_text()
        #logger.debug(f'found book: `{book_title}`')
        return date