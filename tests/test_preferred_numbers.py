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
        self.assertEqual(2, self.sample.digit(3))

        self.assertEqual(2, self.sample.digit(6))

        self.assertEqual(2, self.sample.digit(12))

        self.assertEqual(2, self.sample.digit(24))

        self.assertEqual(3, self.sample.digit(48))

        self.assertEqual(3, self.sample.digit(96))

        self.assertEqual(3, self.sample.digit(192))


    def test_value(self) -> None:
        """Test the value method.
        
        Args:
            None

        Returns:
            None
        """
        self.assertEqual(10, self.sample.value(3, 0))

        self.assertEqual(15, self.sample.value(6, 1))

        self.assertEqual(22, self.sample.value(12, 4))

        self.assertEqual(16, self.sample.value(24, 5))
        
        self.assertEqual(422, self.sample.value(48, 30))

        self.assertEqual(536, self.sample.value(96, 70))

        self.assertEqual(101, self.sample.value(192, 1))
    
        
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
        self.assertEqual([10, 22, 47], self.sample.values(3))

        self.assertEqual([10, 15, 22, 33, 47, 68], self.sample.values(6))

        self.assertEqual([10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82], self.sample.values(12))

        self.assertEqual(24, len(self.sample.values(24)))

        self.assertEqual(48, len(self.sample.values(48)))

        self.assertEqual(96, len(self.sample.values(96)))

        self.assertEqual(192, len(self.sample.values(192)))


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

