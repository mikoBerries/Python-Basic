"This module to Test capitalize.py"
import unittest
import capitalize

class TestCapitalize(unittest.TestCase):
    " Text class caplitalise"
    def test_one_word(self):
        " Tsting capitalize func one word input"
        expected= 'Python'
        text= 'python'
        result = capitalize.cap_text(text)
        self.assertEqual(result,expected)

    def test_multiple_word(self):
        " Tsting capitalize func mutiple word input"
        expected= 'Python Something'
        text= 'python something'
        result = capitalize.cap_text(text)
        self.assertEqual(result,expected)


if __name__=='__main__':
    unittest.main()


# run this class in cli
# py capitalize_test.py