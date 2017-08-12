import unittest
import word_ladder
import re
from unittest.mock import patch


import logging

class TestUserInput(unittest.TestCase):
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
    
    # Mock Input
    @patch('builtins.input', side_effect=['lead', 'gold'])
    def test_user_input7(self, input):
        words = word_ladder.init()
        self.assertEqual(words[0], 'lead')
        self.assertEqual(words[1], 'gold')
    


class TestHelperFunctions(unittest.TestCase):
    def test_same_function(self):
        self.assertEqual(word_ladder.same("lead", "lead"), 4)
        self.assertEqual(word_ladder.same("lead", "mead"), 3)
        self.assertEqual(word_ladder.same("hello", "there"), 0)

    def test_build_basic_function(self):
        ### Arrange ###
        # Create sample dictionary (subset)
        words = ['load', 'toad', 'gold', 'here', 'that', 'this', 'mild', 'wild']
        # Create sample visited
        visited = dict.fromkeys(['toad', 'load'])
        visited_empty = {}

        ### Act ###
        # Create without visited
        adjacent = word_ladder.build_basic(words, visited_empty, 'goad')
        # Create with visited words
        adjacent_visited = word_ladder.build_basic(words, visited, 'goad')

        ### Assert ###
        # Test without visited
        self.assertTrue(all (x in ['load', 'gold', 'toad'] for x in adjacent))
        self.assertTrue(not all (x in ['here', 'that', 'this', 'mild', 'wild'] for x in adjacent))
        # Test with visited words
        print(adjacent_visited)
        self.assertTrue('gold' in adjacent_visited)
        self.assertTrue(not all(x in ['here', 'that', 'this', 'mild', 'wild', 'load', 'toad'] for x in adjacent_visited))


    def test_build_function(self):
        print()
    
    def test_populate_dictionary_function(self):
        print()



class TestFindFunctions(unittest.TestCase):
    def test_recursive_find_function(self):
        print()


    def test_bfs_find_function(self):
        print()


class TestSystem():
    # Mock all inputs
    def test_full_system_recursive(self):
        print()


    def test_full_system_bfs(self):
        print()

if __name__ == '__main__':
    unittest.main(verbosity=2)
