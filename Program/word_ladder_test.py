import unittest
import word_ladder


class word_ladder_test(unittest.TestCase):
    def same_function(self):
        self.assertEqual(word_ladder.same("lead", "lead"), 4)

    def same_function2(self):
        self.assertEqual(word_ladder.same("lead", "this"), 0)


if __name__ == '__main__':
    unittest.main()
