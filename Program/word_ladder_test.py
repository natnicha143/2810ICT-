import unittest
import word_ladder
import re

class word_ladder_test(unittest.TestCase):
    def input_validation_tests(self):
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain'):
            # Code to test
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain'):
            # Code to test
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain'):
            # Code to test
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain'):
            # Code to test
        with self.assertWarnsRegex(UserWarning, 'Start and target words cannot be the same'):
            # Code to test
        with self.assertWarnsRegex(UserWarning, 'Start and target words must be the same length'):
            # Code to test
        with self.assertWarnsRegex(UserWarning, 'Start and target words must be the same length'):
            # Code to test
        with self.assertWarnsRegex(UserWarning, 'Dictionary file not found'):
            # Code to test

    def dictionary_population_tests();
        


    def same_function_tests(self):
        self.assertEqual(word_ladder.same("lead", "lead"), 4)
        self.assertEqual(word_ladder.same("lead", "mead"), 3)
        self.assertEqual(word_ladder.same("hello", "there"), 0)



if __name__ == '__main__':
    unittest.main()
