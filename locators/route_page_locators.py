# find things within a route page

class RoutePagePrinterLocators:
    NAME = 'div.col-xs-12 h2'
    DESCRIPTION = 'div.col-xs-12 h3.mt-1' # was div.fr-view, changed to target title then use sibling
    PROTECTION = 'div.col-xs-12 div.fr-view'
    PHOTOS = 'img.lazy.img-fluid'
    COMMENTS = 'div.comment-body'