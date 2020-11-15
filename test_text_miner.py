from text_miners import bolt_text_bad
import unittest #import TestCase

class TestTextMiner(unittest.TestCase):
    def test_button_head(self):
        text = 'There is a button head bolt'
        self.assertTrue(bolt_text_bad(text))
    
    def test_good_sent_bad_sent(self): #fail
        text = 'there is a good hanger. There is a bad crimp'
        self.assertFalse(bolt_text_bad(text))

    def test_missing(self): #fail
        text = 'The hanger is missing'
        self.assertTrue(bolt_text_bad(text))
    
    def test_one_sent_good(self):
        text = 'There is a good bolt.'
        self.assertFalse(bolt_text_bad(text))

    def test_one_sent_bad(self):
        text = 'There is a bad bolt.'
        self.assertTrue(bolt_text_bad(text))

    def test_permas(self): #fail
        text = 'the permas are worn'
        self.assertTrue(bolt_text_bad(text))

    def test_quarter_inch(self):
        text = 'There is a quarter-inch bolt'
        self.assertTrue(bolt_text_bad(text))
    
    def test_replace(self): #fail
        text = 'the bolt should be replaced'
        self.assertTrue(bolt_text_bad(text))
    
    def test_replace_verb(self): #fail
        text = 'Someone should replace the rings'
        self.assertTrue(bolt_text_bad(text))
    
    def test_rust(self): #fail
        text = 'The hanger is rusted'
        self.assertTrue(bolt_text_bad(text))

    def test_spinning(self): #fail # look for lemma spin in sent with hardware
        text = 'The bolt spins. There is a bad crimp'
        self.assertFalse(bolt_text_bad(text))
    
    def test_star_drive(self):
        text = 'There is a star-drive bolt' #look for words star and drive in same sentence
        self.assertTrue(bolt_text_bad(text))

    
    

if __name__ == '__main__':
    unittest.main()