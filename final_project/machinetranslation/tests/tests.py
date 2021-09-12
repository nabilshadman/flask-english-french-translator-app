import unittest
import sys

from pathlib import Path
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Lundi'), 'Monday')
        self.assertNotEqual(french_to_english('Dimanche'), 'Monday')
        self.assertEqual(french_to_english(), 'No text was provided')
        self.assertEqual(french_to_english('Hello'), 'Hello')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Monday'), 'Lundi')
        self.assertNotEqual(english_to_french('Sunday'), 'Lundi')
        self.assertEqual(english_to_french(), 'No text was provided')
        self.assertEqual(english_to_french('Bonjour'), 'Bonjour')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

if __name__ == '__main__': 
    unittest.main()
