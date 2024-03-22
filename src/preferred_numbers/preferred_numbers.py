
class PreferredNumbers:
    """Provide the preferred number series and its values.
    e.g.) E12: [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
    """

    # The index of the E-series: [3, 6, 12, 24, 48, 96, 192]
    _series_number_e = [3 * 2 ** i for i in range(7)]
    
    _digits_e = [2, 2, 2, 2, 3, 3, 3]

    _torelance_e = [0.4, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]

    _values_e = [
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
    def digits_e(series_number: int) -> int:
        """Returns the number of digits in the E-series.

        Args:
            series_number: The number of the E-series from [3, 6, 12, 24, 48, 96, 192]

        Returns:
            The number of digits in the E-series: 2 or 3

        >>> PreferredNumbers.digits_e(6)
        2
        """
        PreferredNumbers.check_series_e(series_number)

        series_index = PreferredNumbers._series_number_e.index(series_number)

        return PreferredNumbers._digits_e[series_index]
    
    @staticmethod
    def value_e(series_number: int, step: int) -> int:
        """Returns the value in the E-series.

        Args:
            series_number: The number of the E-series from [3, 6, 12, 24, 48, 96, 192]
            step: The index of step in the specified series

        Returns:
            The value in the E-series

        >>> PreferredNumbers.value_e(3, 0)
        10
        """
        PreferredNumbers.check_series_e(series_number)
        PreferredNumbers.check_step_e(series_number, step)

        series_index = PreferredNumbers._series_number_e.index(series_number)

        return PreferredNumbers._values_e[series_index][step]
    
    @staticmethod
    def values_e(series_number: int) -> list:
        """Returns the list of values of the E-series.

        Args:
            series_number: The index of the series from [3, 6, 12, 24, 48, 96, 192]

        Returns:
            The list of values in the E-series
            
        >>> PreferredNumbers.values_e(3)
        [10, 22, 47]
        """
        PreferredNumbers.check_series_e(series_number)

        series_index = PreferredNumbers._series_number_e.index(series_number)
        
        return PreferredNumbers._values_e[series_index].copy()

    @staticmethod
    def check_series_e(series_number: int) -> None:
        """Check if the series is valid for E-series.

        Args:
            series_number: The index of the series from [3, 6, 12, 24, 48, 96, 192]

        Returns:
            None

        >>> PreferredNumbers.check_series_e(3)
        """
        if not series_number in PreferredNumbers._series_number_e:
            raise ValueError(f"Series index must be a value in {PreferredNumbers._series_number_e}: Provided series index {series_number}")
        
    @staticmethod
    def check_step_e(series_number: int, step: int) -> None:
        """Check if the step is valid for E-series.

        Args:
            series_number: The index of the series from [3, 6, 12, 24, 48, 96, 192]
            step: The index of the value in the E-series

        Returns:
            None

        >>> PreferredNumbers.check_step_e(3, 0)
        """
        if step < 0 or series_number <= step:
            raise ValueError(f"Step must be in range 0 to {series_number}: Provided step {step}")


    # R-series
    _series_number_r = [5, 10, 20, 40, 80]

    _values_r = [
        # R5
        [100, 160, 250, 400, 630],
        
        # R10
        [100, 125, 160, 200, 250, 315, 400, 500, 630, 800],

        # R20
        [
            100, 112, 125, 140,
            160, 180, 200, 224,
            250, 280, 315, 355,
            400, 450, 500, 560,
            630, 710, 800, 900
        ],

        # R40
        [
            100, 106, 112, 118, 125, 132, 140, 150,
            160, 170, 180, 190, 200, 212, 224, 236,
            250, 265, 280, 300, 315, 335, 355, 375,
            400, 425, 450, 475, 500, 530, 560, 600,
            630, 670, 710, 750, 800, 850, 900, 950
        ],

        # R80
        [
            100, 103, 106, 109, 112, 115, 118, 122,
            125, 128, 132, 136, 140, 145, 150, 155,
            160, 165, 170, 175, 180, 185, 190, 195,
            200, 206, 212, 218, 224, 230, 236, 243,
            250, 258, 265, 272, 280, 290, 300, 307,
            315, 325, 335, 345, 355, 365, 375, 387,
            400, 412, 425, 437, 450, 462, 475, 487,
            500, 515, 530, 545, 560, 580, 600, 615,
            630, 650, 670, 690, 710, 730, 750, 775,
            800, 825, 850, 875, 900, 925, 950, 975
        ]
    ]

    @staticmethod
    def value_r(series_number: int, step: int) -> int:
        """Returns the value in the R-series.

        Args:
            series_number: The number of the R-series from [5, 10, 20, 40, 80]
            step: The index of step in the specified series

        Returns:
            The value in the R-series

        >>> PreferredNumbers.value_r(5, 0)
        100
        """
        PreferredNumbers.check_series_r(series_number)
        PreferredNumbers.check_step_r(series_number, step)

        series_index = PreferredNumbers._series_number_r.index(series_number)

        return PreferredNumbers._values_r[series_index][step]
    
    @staticmethod
    def values_r(series_number: int) -> list:
        """Returns the list of values of the R-series.

        Args:
            series_number: The index of the series from [5, 10, 20, 40, 80]

        Returns:
            The list of values in the R-series
            
        >>> PreferredNumbers.values_r(5)
        [100, 160, 250, 400, 630]
        """
        PreferredNumbers.check_series_r(series_number)

        series_index = PreferredNumbers._series_number_r.index(series_number)
        
        return PreferredNumbers._values_r[series_index].copy()
    
    @staticmethod
    def check_series_r(series_number: int) -> None:
        """Check if the series is valid for R-series.

        Args:
            series_number: The index of the series from [5, 10, 20, 40, 80]

        Returns:
            None

        >>> PreferredNumbers.check_series_r(5)
        """
        if not series_number in PreferredNumbers._series_number_r:
            raise ValueError(f"Series index must be a value in {PreferredNumbers._series_number_r}: Provided series index {series_number}")
        
    @staticmethod
    def check_step_r(series_number: int, step: int) -> None:
        """Check if the step is valid for R-series.

        Args:
            series_number: The index of the series from [5, 10, 20, 40, 80]
            step: The index of the value in the R-series

        Returns:
            None

        >>> PreferredNumbers.check_step_r(5, 0)
        """
        if step < 0 or series_number <= step:
            raise ValueError(f"Step must be in range 0 to {series_number}: Provided step {step}")