from storage import database
from pages.route_page import RoutePage
from pages.area_page import AreaPage


USER_CHOICE = '''What would you like to do:
- 'a' for search new area
- 'r' for search new route
- 'l' for list all routes
- 'f' for list flagged routes
- 'd' to delete a route
- 'q' to quit
- 'c' to clear database

Your choice: '''


def list_routes():
    for route in database.get_all_routes():
        flag = 'YES' if route[4] else 'NO'  # book[3] will be a falsy value (0) if not read
        print(f'{route[1]}, link: {route[2]} — Bad Gear: {flag}, Ref: {route[4]}')


def list_flagged_routes():
    for route in database.get_flagged_routes():
        flag = 'YES' if route[4] else 'NO'  # book[3] will be a falsy value (0) if not read
        print(f'{route[1]}, link: {route[2]} — Bad Gear: {flag}, Ref: {route[4]}')


def add_route():
    url = input('Enter url: ')
    database.add_route(RoutePage(url))


def add_area_wrapper():
    url = input('Enter url: ')
    area = AreaPage(url)
    add_area_recursive(area)


def add_area_recursive(area):
    if area.sub_type == 'Routes': #terminates recursion
        for climb in area.subcomponent:
            database.add_route(climb)
    else:
        for area in area.subcomponent:
            add_area_recursive(area)


def delete_route():
    name = input('Enter the name of the route you wish to delete: ')
    database.delete_route(name)

def clear_database():
    database.clear()




menu_choices = {
    'a': add_area_wrapper,
    'r': add_route,
    'l': list_routes,
    'f': list_flagged_routes,
    'd': delete_route,
    'c': clear_database
}

def menu():
    database.create_check_route_table()
    chosen = input(USER_CHOICE)
    while chosen != 'q':
        if chosen in { 'a', 'r', 'l', 'f', 'd', 'c' }:
            menu_choices[chosen]()
        else:
            print('Invalid input')
        chosen = input(USER_CHOICE)

menu()