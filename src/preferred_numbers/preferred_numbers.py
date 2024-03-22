
class PreferredNumbers:
    """Provide the preferred number series and its values.
    e.g.) E12: [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
    """

    # The index of the series from [3, 6, 12, 24, 48, 96, 192]
    series_index = [3 * 2 ** i for i in range(7)]
    
    digits = [2, 2, 2, 2, 3, 3, 3]

    torelance = [0.4, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]

    e_series = [
        # E3
        [10, 22, 47],

        #E6
        [10, 15, 22, 33, 47, 68],
        
        #E12
        [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82],
        
        #E24
        [
            10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30,
            33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91
        ],
        
        #E48
        [
            100, 105, 110, 115, 121, 127, 133, 140, 147, 154, 162, 169,
            178, 187, 196, 205, 215, 226, 237, 249, 261, 274, 287, 301,
            316, 332, 348, 365, 383, 402, 422, 442, 464, 487, 511, 536,
            562, 590, 619, 649, 681, 715, 750, 787, 825, 866, 909, 953
        ],
        
        #E96
        [
            100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130,
            133, 137, 140, 143, 147, 150, 154, 158, 162, 165, 169, 174,
            178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232,
            237, 243, 249, 255, 261, 267, 274, 280, 287, 294, 301, 309,
            316, 324, 332, 340, 348, 357, 365, 374, 383, 392, 402, 412,
            422, 432, 442, 453, 464, 475, 487, 499, 511, 523, 536, 549,
            562, 576, 590, 604, 619, 634, 649, 665, 681, 698, 715, 732,
            750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976
        ],
        
        #E192
        [
            100, 101, 102, 104, 105, 106, 107, 109, 110, 111, 113, 114,
            115, 117, 118, 120, 121, 123, 124, 126, 127, 129, 130, 132,
            133, 135, 137, 138, 140, 142, 143, 145, 147, 149, 150, 152,
            154, 156, 158, 160, 162, 164, 165, 167, 169, 172, 174, 176,
            178, 180, 182, 184, 187, 189, 191, 193, 196, 198, 200, 203,
            205, 208, 210, 213, 215, 218, 221, 223, 226, 229, 232, 234,
            237, 240, 243, 246, 249, 252, 255, 258, 261, 264, 267, 271,
            274, 277, 280, 284, 287, 291, 294, 298, 301, 305, 309, 312,
            316, 320, 324, 328, 332, 336, 340, 344, 348, 352, 357, 361,
            365, 370, 374, 379, 383, 388, 392, 397, 402, 407, 412, 417,
            422, 427, 432, 437, 442, 448, 453, 459, 464, 470, 475, 481,
            487, 493, 499, 505, 511, 517, 523, 530, 536, 542, 549, 556,
            562, 569, 576, 583, 590, 597, 604, 612, 619, 626, 634, 642,
            649, 657, 665, 673, 681, 690, 698, 706, 715, 723, 732, 741,
            750, 759, 768, 777, 787, 796, 806, 816, 825, 835, 845, 856,
            866, 876, 887, 898, 909, 920, 931, 942, 953, 965, 976, 988
        ],
    ]

    @staticmethod
    def digit(series: int) -> int:
        """Returns the number of digits in the series.

        Args:
            series: The index of the series from [3, 6, 12, 24, 48, 96, 192]

        Returns:
            The number of digits in the series: 2 or 3

        >>> PreferredNumbers.digit(6)
        2
        """
        PreferredNumbers.check_series(series)

        series_index = PreferredNumbers.series_index.index(series)
        return PreferredNumbers.digits[series_index]
    
    @staticmethod
    def value(series: int, step: int) -> int:
        """Returns the value of the preferred number.

        Args:
            series: The index of the series from [3, 6, 12, 24, 48, 96, 192]
            step: The index of the value in the series

        Returns:
            The value of the preferred number

        >>> PreferredNumbers.value(3, 0)
        10
        """
        PreferredNumbers.check_series(series)

        series_index = PreferredNumbers.series_index.index(series)

        PreferredNumbers.check_step(series, step)

        return PreferredNumbers.e_series[series_index][step]
    
    @staticmethod
    def values(series: int) -> list:
        """Returns the list of values of the preferred number series.

        Args:
            series: The index of the series from [3, 6, 12, 24, 48, 96, 192]

        Returns:
            The list of values of the preferred number series
            
        >>> PreferredNumbers.values(3)
        [10, 22, 47]
        """
        PreferredNumbers.check_series(series)

        series_index = PreferredNumbers.series_index.index(series)
        return PreferredNumbers.e_series[series_index].copy()

    @staticmethod
    def check_series(series: int) -> None:
        """Check if the series is valid.

        Args:
            series: The index of the series from [3, 6, 12, 24, 48, 96, 192]

        Returns:
            None

        >>> PreferredNumbers.check_series(3)
        """
        if not series in PreferredNumbers.series_index:
            raise ValueError(f"Series index must be a value in {PreferredNumbers.series_index}: Provided series index {series}")
        
    @staticmethod
    def check_step(series: int, step: int) -> None:
        """Check if the step is valid.

        Args:
            series: The index of the series from [3, 6, 12, 24, 48, 96, 192]
            step: The index of the value in the series

        Returns:
            None

        >>> PreferredNumbers.check_step(3, 0)
        """
        if step < 0 or len(PreferredNumbers.e_series[PreferredNumbers.series_index.index(series)]) <= step:
            raise ValueError(f"Step must be in range 0 to {len(PreferredNumbers.e_series[PreferredNumbers.series_index.index(series)])}: Provided step {step}")
