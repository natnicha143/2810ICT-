import unittest
import word_ladder
import re
from unittest.mock import patch
from io import StringIO


import logging

class TestUserInput(unittest.TestCase):
    # Mock input
    @patch('builtins.input', side_effect=['le1d', 'gold'])
    def test_user_input1(self, input):
        # Assert that the raised UserWarning is correct for the test case
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain numbers or special characters'):
         # Ensure the program exits after the warning
            with self.assertRaises(SystemExit):              
                word_ladder.init()
    
    # Mock Input
    @patch('builtins.input', side_effect=['lead', 'go@d'])
    def test_user_input2(self, input):
        # Assert that the raised UserWarning is correct for the test case
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain numbers or special characters'):
            # Ensure the program exits after the warning
            with self.assertRaises(SystemExit):                 
                word_ladder.init()
    
    # Mock Input
    @patch('builtins.input', side_effect=['he_s', 's_da'])
    def test_user_input3(self, input):
        # Assert that the raised UserWarning is correct for the test case
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain numbers or special characters'):
            # Ensure the program exits after the warning
            with self.assertRaises(SystemExit):                 
                word_ladder.init()
    
    # Mock Input
    @patch('builtins.input', side_effect=['hell3', 'ther3'])
    def test_user_input4(self, input):
        # Assert that the raised UserWarning is correct for the test case
        with self.assertWarnsRegex(UserWarning, 'Input words cannot contain numbers or special characters'):
            # Ensure the program exits after the warning
            with self.assertRaises(SystemExit):                 
                word_ladder.init()
    
    # Mock Input
    @patch('builtins.input', side_effect=['lead', 'lead'])
    def test_user_input5(self, input):
        # Assert that the raised UserWarning is correct for the test case
        with self.assertWarnsRegex(UserWarning, 'Start and target words cannot be the same'):
            # Ensure the program exits after the warning
            with self.assertRaises(SystemExit):                 
                word_ladder.init()
    
    # Mock Input
    @patch('builtins.input', side_effect=['hello', 'test'])
    def test_user_input6(self, input):
        # Assert that the raised UserWarning is correct for the test case
        with self.assertWarnsRegex(UserWarning, 'Start and target words must be the same length'):
            # Ensure the program exits after the warning
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
        self.assertTrue('gold' in adjacent_visited)
        self.assertTrue(not all(x in ['here', 'that', 'this', 'mild', 'wild', 'load', 'toad'] for x in adjacent_visited))


    def test_build_function(self):
        ### Arrange
        source_word = "abcd"
        words = ["xbcd", "axcd", "abxd", "abcx", "vbcd"]
        visited = dict.fromkeys(["vbcd"])
        adjacent = []

        ### Act
        # Iterate the wildcard through each position of the regex pattern
        for i in range(len(source_word)):
            adjacent += word_ladder.build(source_word[:i] + "." + source_word[i + 1:], words, visited, adjacent)
        
        ### Assert
        self.assertTrue(all (x in ["xbcd", "axcd", "abxd", "abcx"] for x in adjacent))
        self.assertTrue("vbcd" not in adjacent)

    
    def test_populate_dictionary_function(self):
        ### Arrange
        # File contains
        # 3x | 3 Letter Words
        # 4x | 4 Letter Words
        # 5x | 5 Letter Words
        test_word_file = "test_data/subset.txt"

        ### Act
        words_3 = word_ladder.populate_dictionary(test_word_file, 3)
        words_4 = word_ladder.populate_dictionary(test_word_file, 4)
        words_5 = word_ladder.populate_dictionary(test_word_file, 5)

        ### Assert
        self.assertEqual(len(words_3), 3)
        self.assertEqual(len(words_4), 4)
        self.assertEqual(len(words_5), 5)


    def test_populate_dictionary_function_banned_words(self):
        ### Arrange
        # File contains
        # 3x | 3 Letter Words
        # 4x | 4 Letter Words
        # 5x | 5 Letter Words
        test_word_file = "test_data/subset.txt"
        banned_word_file = "test_data/subset_banned.txt"

        ### Act
        words_3 = word_ladder.populate_dictionary(test_word_file, 3, banned_word_file)
        words_4 = word_ladder.populate_dictionary(test_word_file, 4, banned_word_file)
        words_5 = word_ladder.populate_dictionary(test_word_file, 5, banned_word_file)

        ### Assert
        self.assertEqual(len(words_3), 2)
        self.assertTrue("are" not in words_3)
        self.assertEqual(len(words_4), 3)
        self.assertTrue("then" not in words_4)
        self.assertEqual(len(words_5), 4)
        self.assertTrue("speck" not in words_5)



class TestSystem(unittest.TestCase):
    # Mock all inputs | Runs in recursive mode
    @patch('builtins.input', side_effect=['dictionary', 'lead', 'gold', '', ''])
    def test_full_system_recursive_LG(self, input):
        ### Act
        # Patch sys.stdout to a StringIO object called fake_stdout
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            word_ladder.run()
        
        ### Assert
        self.assertEqual("3\t['lead', 'load', 'goad', 'gold']\n", fake_stdout.getvalue())


    # Mock all inputs | Runs in BFS mode
    @patch('builtins.input', side_effect=['dictionary', 'lead', 'gold', '', 'y'])
    def test_full_system_bfs(self, input):
        ### Act
        # Patch sys.stdout to a StringIO object called fake_stdout
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            word_ladder.run()

        ### Assert
        self.assertEqual("3\t['lead', 'load', 'goad', 'gold']\n", fake_stdout.getvalue())



if __name__ == '__main__':
    unittest.main(verbosity=2)
