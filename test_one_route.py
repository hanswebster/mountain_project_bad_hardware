from pages.route_page import RoutePage
import unittest #import TestCase

class TestRoute(unittest.TestCase):
    def test_no_comments(self): 
        url = 'https://www.mountainproject.com/route/119937569/dalle-a-droite'
        route = RoutePage(url)
        self.assertFalse(route.bad_gear)

    def test_flag_comment_no_location_no_photos(self):
        url = 'https://www.mountainproject.com/route/105755620/knot-carrot'
        route = RoutePage(url)
        self.assertTrue(route.bad_gear)

    def test_flag_desc(self):
        url = 'https://www.mountainproject.com/route/105901424/endgame'
        route = RoutePage(url)
        self.assertTrue(route.bad_gear)

    def test_no_pro_or_desc(self): #boulder
        url = 'https://www.mountainproject.com/route/119937725/unnamed-v1'
        route = RoutePage(url)
        self.assertFalse(route.bad_gear)

    def test_flag_photos(self):
        url = 'https://www.mountainproject.com/area/106345780/playpia-shirahamahachinohe'
        route = RoutePage(url)
        self.assertTrue(route.bad_gear)

    def test_no_flag_1(self): #TODO: Change url
        url = 'https://www.mountainproject.com/route/107528888/feeling-lucky'
        route = RoutePage(url)
        self.assertFalse(route.bad_gear)

    def test_no_flag_2(self): #TODO: Change url
        url = 'https://www.mountainproject.com/route/109538712/hall-of-mirrors'
        route = RoutePage(url)
        self.assertFalse(route.bad_gear)

    def test_no_flag_3(self): #TODO: Change url
        url = 'https://www.mountainproject.com/route/105748816/center-route'
        route = RoutePage(url)
        self.assertFalse(route.bad_gear)

    def test_no_flag_4(self): #TODO: Change url
        url = 'https://www.mountainproject.com/route/105753910/not-my-cross-to-bear'
        route = RoutePage(url)
        self.assertFalse(route.bad_gear)

    def test_no_flag_5(self): #TODO: Change url
        url = 'https://www.mountainproject.com/route/106081917/whip-stocking'
        route = RoutePage(url)
        self.assertFalse(route.bad_gear)

if __name__ == '__main__':
    unittest.main()