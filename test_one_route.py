from pages.route_page import RoutePage
import unittest #import TestCase

class TestRoute(unittest.TestCase):
    def test_no_comments(self):
        pass

    def test_flag_comment(self):
        knot_carrot = 'https://www.mountainproject.com/route/105755620/knot-carrot'
        route = RoutePage(knot_carrot)
        self.assertTrue(route.bad_gear)

    def test_flag_desc(self):
        endgame = 'https://www.mountainproject.com/route/105901424/endgame'
        route = RoutePage(endgame)
        self.assertTrue(route.bad_gear)

    def test_no_protection(self):
        pass

    def test_flag_protection(self):
        pass

    def test_flag_photos(self):
        pass

    def test_no_photos(self):
        pass

    def test_no_flag(self):
        pass

if __name__ == '__main__':
    unittest.main()