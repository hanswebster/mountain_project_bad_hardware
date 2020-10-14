import requests

from pages.route_page import RoutePage
from pages.area_page import AreaPage

'''
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    level=logging.INFO,
    filename='books_log.txt'
)
logger = logging.getLogger('books_app')
'''

'''
page_content = requests.get('https://www.mountainproject.com/route/109070301/black-gold?print=1').content
route_page = RoutePage(page_content)
print(route_page.description)
print(route_page.protection)
print(route_page.photo_captions)
print(route_page.comments)
'''


area_content = requests.get('https://www.mountainproject.com/area/105745870/creek-side').content
printer_area_content = requests.get('https://www.mountainproject.com/area/105745870/creek-side?print=1').content

area_page = AreaPage(area_content, printer_area_content)
print(area_page.name)
print(area_page.description)
print(area_page.comments)
print(area_page.photo_captions)
print(area_page.sub_type)
print(area_page.subcomponent)

