from src.preferred_numbers import PreferredNumbers
from unittest import TestCase

class ExceptPreferredNumber(TestCase):
    """Test class for the PreferredNumber class with exceptions.

    Put the following command in the terminal to run the test:
    python -m unittest preferred_number.py
    """

    def setUp(self) -> None:
        """Create a PreferredNumber object.

        Returns:
            None
        """
        self.sample = PreferredNumbers()


    def test_digit(self) -> None:
        """Test the digit method.
        
        Args:
            None

        Returns:
            None
        """
        test_cases = [
            (3, 2),
            (6, 2),
            (12, 2),
            (24, 2),
            (48, 3),
            (96, 3),
            (192, 3)
        ]

        for input, expected_output in test_cases:
            with self.subTest(input=input, expected_output=expected_output):
                self.assertEqual(expected_output, self.sample.digit(input))

    def test_value(self) -> None:
        """Test the value method.
        
        Args:
            None

        Returns:
            None
        """

        test_cases = [
            (3, 0, 10),
            (6, 1, 15),
            (12, 4, 22),
            (24, 5, 16),
            (48, 30, 422),
            (96, 70, 536),
            (192, 1, 101)
        ]

        for series, step, expected_output in test_cases:
            with self.subTest(series=series, step=step, expected_output=expected_output):
                self.assertEqual(expected_output, self.sample.value(series, step))
   
    def test_values(self) -> None:
        """Test the values method.
        
        Args:
            None

        Returns:
            None
        """

        test_cases = [
            (3, 3),
            (6, 6),
            (12, 12),
            (24, 24),
            (48, 48),
            (96, 96),
            (192, 192)
        ]

        for input, expected_output in test_cases:
            with self.subTest(input=input, expected_output=expected_output):
                self.assertEqual(expected_output, len(self.sample.values(input)))


    def test_check_series(self) -> None:
        """Test the check_series method.
        
        Args:
            None

        Returns:
            None
        """
        success_case = [ 3, 6, 12, 24, 48, 96, 192 ]
        fail_case = [ 1, 2, 4, 5, 7, 8, 16, 32, 64, 128, 256]

        for input in success_case:
            with self.subTest(input=input):
                self.assertIsNone(self.sample.check_series(input))

        for input in fail_case:
            with self.subTest(input=input):
                with self.assertRaises(ValueError) as context:
                    self.sample.check_series(input)
                self.assertEqual(f"Series index must be a value in {success_case}: Provided series index {input}", str(context.exception))


    def test_check_step(self) -> None:
        """Test the check_step method.
        
        Args:
            None

        Returns:
            None
        """
        success_case = [
            (3, 0),
            (3, 2),
            (192, 0),
            (192, 191),
        ]
        fail_case = [
            (3, -1),
            (3, 3),
            (192, -1),
            (192, 192),
        ]

        for series, step in success_case:
            with self.subTest(series=series, step=step):
                self.assertIsNone(self.sample.check_step(series, step))

        for series, step in fail_case:
            with self.subTest(series=series, step=step):
                with self.assertRaises(ValueError) as context:
                    self.sample.check_step(series, step)
                self.assertEqual(f"Step must be in range 0 to {len(self.sample.e_series[self.sample.series_index.index(series)])}: Provided step {step}", str(context.exception))

    def tearDown(self) -> None:
        """Delete the PreferredNumber object.
        
        Args:
            None

        Returns:
            None
        """
        del self.sample

