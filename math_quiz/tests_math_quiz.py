import unittest
from math_quiz import GetRandomInteger, GetRandomOperator, CalculateResult


class TestMathGame(unittest.TestCase):

    def test_GetRandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = GetRandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_GetRandomOperator(self):
        # Test if given operator is +, - or *
        for _ in range(100):
             operator = GetRandomOperator()
             self.assertIn(operator, ['+', '-', '*'])

    def test_CalculateResult(self):
        # Test whether the calculation is assembled correctly and if the result is correct
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '-', '8 - 3', 5),
                (4, 6, '*', '4 * 6', 24)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = CalculateResult(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                
                

if __name__ == "__main__":
    unittest.main()
