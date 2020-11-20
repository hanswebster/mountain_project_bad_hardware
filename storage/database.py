from storage.database_connection import DatabaseConnection


def create_check_route_table():
    with DatabaseConnection('routes.db') as connection:
        cursor = connection.cursor()
        cursor.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='routes' ")
        if cursor.fetchone()[0] == 0:
            cursor.execute('CREATE TABLE routes (id integer primary key, name text, link text, flagged integer, flag_description text default none)')


def get_all_routes():
    with DatabaseConnection('routes.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM routes')
        routes = cursor.fetchall()
    return routes


def get_flagged_routes():
    with DatabaseConnection('routes.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM routes WHERE flagged = 1')
        routes = cursor.fetchall()
    return routes


def add_route(route) -> None:
    with DatabaseConnection('routes.db') as connection:
        cursor = connection.cursor()
        bad_gear = 1 if route.bad_gear else 0
        cursor.execute('INSERT INTO routes (name, link, flagged, flag_description) VALUES (?, ?, ?, ?)', 
            (route.name, route.url, bad_gear, ' - '.join(route.bad_gear)))


def delete_route(name: str) -> None:
    with DatabaseConnection('routes.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM routes WHERE name=?', (name,))

def clear():
    with DatabaseConnection('routes.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM routes')
    print('Cleared route db')