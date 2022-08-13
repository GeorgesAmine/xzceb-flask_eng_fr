import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour', 'incorrect translation')
        self.assertNotEqual(english_to_french('Good night'), 'Bonjour')
        self.assertEqual(english_to_french(''), 'Cannot translate empty text')

class TestFrenchToEnglish(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello', 'incorrect translation')
        self.assertNotEqual(french_to_english('Bonsoir'), 'Good morning')
        self.assertEqual(french_to_english(''), 'Cannot translate empty text')

if __name__ == '__main__':
    unittest.main()