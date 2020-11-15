from pages.route_page import RoutePage
import unittest #import TestCase

class TestRoute(unittest.TestCase):
    def test_no_comments(self): #TODO: Change Url
        knot_carrot = 'https://www.mountainproject.com/route/105755620/knot-carrot'
        route = RoutePage(knot_carrot)
        self.assertTrue(route.bad_gear)

    def test_flag_comment_no_location(self): #done
        knot_carrot = 'https://www.mountainproject.com/route/105755620/knot-carrot'
        route = RoutePage(knot_carrot)
        self.assertTrue(route.bad_gear)

    def test_flag_desc(self): #done
        endgame = 'https://www.mountainproject.com/route/105901424/endgame'
        route = RoutePage(endgame)
        self.assertTrue(route.bad_gear)

    def test_no_protection(self): #TODO: change url to page without pro section (may not be needed)
        knot_carrot = 'https://www.mountainproject.com/route/105755620/knot-carrot'
        route = RoutePage(knot_carrot)
        self.assertTrue(route.bad_gear)

    def test_flag_protection(self): #TODO: Change url
        knot_carrot = 'https://www.mountainproject.com/route/105755620/knot-carrot'
        route = RoutePage(knot_carrot)
        self.assertTrue(route.bad_gear)

    def test_flag_photos(self): #TODO: change url
        knot_carrot = 'https://www.mountainproject.com/route/105755620/knot-carrot'
        route = RoutePage(knot_carrot)
        self.assertTrue(route.bad_gear)

    def test_no_photos(self): #TODO: change url and assert True for False
        knot_carrot = 'https://www.mountainproject.com/route/105755620/knot-carrot'
        route = RoutePage(knot_carrot)
        self.assertTrue(route.bad_gear)

    def test_no_flag(self): #TODO: Change url
        knot_carrot = 'https://www.mountainproject.com/route/105755620/knot-carrot'
        route = RoutePage(knot_carrot)
        self.assertTrue(route.bad_gear)

if __name__ == '__main__':
    unittest.main()