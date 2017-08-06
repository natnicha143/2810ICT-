import unittest
import word_ladder_functions as word_ladder

class WordLadderTest(unittest.TestCase):

    def same_function(self):
        self.assertEqual(word_ladder.same("lead", "gold"), 4)
        self.assertEqual(word_ladder.same("lead", "lead"), 0)


if __name__ == '__main__':
    unittest.main()