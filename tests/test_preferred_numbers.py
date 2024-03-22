from src.preferred_numbers import PreferredNumbers
from unittest import TestCase


class ExceptPreferredNumber(TestCase):
    """Test class for the PreferredNumber class with exceptions.

    Put the following command in the terminal to run the test:
    python -m unittest preferred_number.py
    """

    def setUp(self) -> None:
        self.sample = PreferredNumbers()

    def test_digits_e(self) -> None:
        test_cases = [(3, 2), (6, 2), (12, 2), (24, 2), (48, 3), (96, 3), (192, 3)]

        for input, expected_output in test_cases:
            with self.subTest(input=input, expected_output=expected_output):
                self.assertEqual(expected_output, self.sample.digits_e(input))

    def test_value_e(self) -> None:
        test_cases = [
            (3, 0, 10),
            (6, 1, 15),
            (12, 4, 22),
            (24, 5, 16),
            (48, 30, 422),
            (96, 70, 536),
            (192, 1, 101),
        ]

        for series_number, step, expected_output in test_cases:
            with self.subTest(
                series_number=series_number, step=step, expected_output=expected_output
            ):
                self.assertEqual(
                    expected_output, self.sample.value_e(series_number, step)
                )

    def test_values_e(self) -> None:
        test_cases = [
            (3, 3),
            (6, 6),
            (12, 12),
            (24, 24),
            (48, 48),
            (96, 96),
            (192, 192),
        ]

        for input, expected_output in test_cases:
            with self.subTest(input=input, expected_output=expected_output):
                self.assertEqual(expected_output, len(self.sample.values_e(input)))

    def test_check_series_e(self) -> None:
        success_case = [3, 6, 12, 24, 48, 96, 192]
        fail_case = [1, 2, 4, 5, 7, 8, 16, 32, 64, 128, 256]

        for input in success_case:
            with self.subTest(input=input):
                self.assertIsNone(self.sample.check_series_e(input))

        for input in fail_case:
            with self.subTest(input=input):
                with self.assertRaises(ValueError) as context:
                    self.sample.check_series_e(input)
                self.assertEqual(
                    f"Series index must be a value in {success_case}: "
                    f"Provided series index {input}",
                    str(context.exception),
                )

    def test_check_step_e(self) -> None:
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
                self.assertIsNone(self.sample.check_step_e(series, step))

        for series, step in fail_case:
            with self.subTest(series=series, step=step):
                with self.assertRaises(ValueError) as context:
                    self.sample.check_step_e(series, step)
                self.assertEqual(
                    f"Step must be in range 0 to {series}: Provided step {step}",
                    str(context.exception),
                )

    def test_value_r(self) -> None:
        test_cases = [
            (5, 0, 100),
            (10, 1, 125),
            (20, 4, 160),
            (40, 5, 132),
            (80, 30, 236),
        ]

        for series_number, step, expected_output in test_cases:
            with self.subTest(
                series_number=series_number, step=step, expected_output=expected_output
            ):
                self.assertEqual(
                    expected_output, self.sample.value_r(series_number, step)
                )

    def test_values_r(self) -> None:
        test_cases = [(5, 5), (10, 10), (20, 20), (40, 40), (80, 80)]

        for input, expected_output in test_cases:
            with self.subTest(input=input, expected_output=expected_output):
                self.assertEqual(expected_output, len(self.sample.values_r(input)))

    def test_check_series_r(self) -> None:
        success_case = [5, 10, 20, 40, 80]
        fail_case = [1, 2, 4, 8, 16, 32, 64, 128, 256]

        for input in success_case:
            with self.subTest(input=input):
                self.assertIsNone(self.sample.check_series_r(input))

        for input in fail_case:
            with self.subTest(input=input):
                with self.assertRaises(ValueError) as context:
                    self.sample.check_series_r(input)
                self.assertEqual(
                    "Series index must be a value in [5, 10, 20, 40, 80]: "
                    f"Provided series index {input}",
                    str(context.exception),
                )

    def test_check_step_r(self) -> None:
        success_case = [
            (5, 0),
            (5, 4),
            (80, 0),
            (80, 79),
        ]
        fail_case = [
            (5, -1),
            (5, 5),
            (80, -1),
            (80, 80),
        ]

        for series, step in success_case:
            with self.subTest(series=series, step=step):
                self.assertIsNone(self.sample.check_step_r(series, step))

        for series, step in fail_case:
            with self.subTest(series=series, step=step):
                with self.assertRaises(ValueError) as context:
                    self.sample.check_step_r(series, step)
                self.assertEqual(
                    f"Step must be in range 0 to {series}: Provided step {step}",
                    str(context.exception),
                )

    def tearDown(self) -> None:
        del self.sample
