import unittest
from math_quiz import create_random_int,select_math_operation, calculate_random_operation


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = create_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test__math_operation(self):
        valid_operations = {'+', '-', '*'} # Only these operations should be generated
        for i in range(100):  # Run multiple times to check for validity over many samples
            operation = select_math_operation()
            self.assertIn(operation, valid_operations)

    def test_calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (7, 3,'-','7 - 3', 4),
                (3, 0, '+', '3 + 0', 3),
                (2, 0, '*', '2 * 0', 0),
                (1, 1, '-', '1 - 1', 0),
                (4, 3, '*', '4 * 3', 12)

            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                question, answer = calculate_random_operation(num1,num2,operator)
                self.assertEqual(question, expected_problem)
                self.assertEqual(answer, expected_answer)
                

if __name__ == "__main__":
    unittest.main()
