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
        
        with self.assertRaises(ValueError) as context:
            self.sample.value(24, -1)
        self.assertEqual("Step must be less than 24: Provided step -1", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.sample.value(3, 24)
        self.assertEqual("Step must be less than 3: Provided step 24", str(context.exception))

   
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

        with self.assertRaises(ValueError) as context:
            self.sample.values(1)
        self.assertEqual("Series index must be a value in [3, 6, 12, 24, 48, 96, 192]: Provided series index 1", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.sample.values(4)

        self.assertEqual("Series index must be a value in [3, 6, 12, 24, 48, 96, 192]: Provided series index 4", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.sample.values(384)

        self.assertEqual("Series index must be a value in [3, 6, 12, 24, 48, 96, 192]: Provided series index 384", str(context.exception))


    def tearDown(self) -> None:
        """Delete the PreferredNumber object.
        
        Args:
            None

        Returns:
            None
        """
        del self.sample

