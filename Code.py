# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Bonus requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

import unittest
class Anagrams:

    def __init__(self):
        self.words = open('qualcomm-test-words.txt').readlines()

    def get_anagrams(self, word):
        sorted_word = ''.join(sorted(word.strip()))
        return [word.strip() for word in self.words if ''.join(sorted(word.strip())) == sorted_word]


class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        anagrams = Anagrams()

        # Test case 1: Anagrams for 'plates'
        self.assertEquals(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])

        # Test case 2: Anagrams for 'eat'
        self.assertEquals(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])

        # Test case 3: Anagrams for 'stop'
        self.assertEqual(anagrams.get_anagrams('stop'), ['opts', 'post','pots', 'spot', 'stop', 'tops'])

        # Test case 4: Anagrams for 'silent'
        self.assertEqual(anagrams.get_anagrams('silent'), ['enlist', 'inlets','listen', 'silent'])


if __name__ == '__main__':
    unittest.main()
