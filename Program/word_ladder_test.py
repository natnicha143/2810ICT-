import unittest
import word_ladder

class word_ladder_test(unittest.TestCase):
    # def test_solution_length(self):
    #     self.assertEqual(find(), 3) 

    def same_function(self):
        self.assertEqual(word_ladder.same("lead", "lead"), 0)
        self.assertEqual(word_ladder.same("lead", "gold"), 3)

if __name__ == '__main__':
    unittest.main(exit=True)