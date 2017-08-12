import unittest
import word_ladder
import re
from unittest.mock import patch

import logging

class WordLadderTest(unittest.TestCase):

    # Mock input
    @patch('builtins.input', side_effect=['le1d', 'gold'])
    def test_user_input1(self, input):
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain numbers or special characters'):
            with self.assertRaises(SystemExit):              
                word_ladder.init()
    
    # Mock Input
    @patch('builtins.input', side_effect=['lead', 'go@d'])
    def test_user_input2(self, input):
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain numbers or special characters'):
            with self.assertRaises(SystemExit):                 
                word_ladder.init()
    
    # Mock Input
    @patch('builtins.input', side_effect=['he_s', 'as_da'])
    def test_user_input3(self, input):
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain numbers or special characters'):
            with self.assertRaises(SystemExit):                 
                word_ladder.init()
    
    # Mock Input
    @patch('builtins.input', side_effect=['hell3', 'ther3'])
    def test_user_input4(self, input):
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain numbers or special characters'):
            with self.assertRaises(SystemExit):                 
                word_ladder.init()
    
    # Mock Input
    @patch('builtins.input', side_effect=['lead', 'lead'])
    def test_user_input5(self, input):
        with self.assertWarnsRegex(UserWarning, 'Start and target words cannot be the same'):
            with self.assertRaises(SystemExit):                 
                word_ladder.init()
    
    # Mock Input
    @patch('builtins.input', side_effect=['hello', 'test'])
    def test_user_input6(self, input):
        with self.assertWarnsRegex(UserWarning, 'Start and target words must be the same length'):
            with self.assertRaises(SystemExit):                 
                word_ladder.init()
    
    # # Mock Input
    # @patch('builtins.input', side_effects=['lead', 'gold'])
    # def test_user_input7(self, input):
    #     self.longMessage = True
    #     msg_out = str(input()) + ', ' + str(input())
    #     self.assertEqual(1, 2, msg=msg_out)
    

    
    
    # Mock Input
    # @mock.patch('builtins.input', side_effects=['', ''])
    # def test_user_init():
    #     with self.assertWarnsRegex(UserWarning, 'Dictionary file not found'):
    #         with self.assertRaises(SystemExit):                 
    #             word_ladder.init()

    # def dictionary_population_tests();

    def same_function_tests(self):
        self.assertEqual(word_ladder.same("lead", "lead"), 4)
        self.assertEqual(word_ladder.same("lead", "mead"), 3)
        self.assertEqual(word_ladder.same("hello", "there"), 0)



if __name__ == '__main__':
    unittest.main(verbosity=1)
