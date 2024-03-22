# Providing Preferred numbers

Fetch preferred numbers from the E-series and R-series.

* E-series:
  - 2 digits: E3, E6, E12, E24
  - 3 digits: E48, E96, E192
* R-series:
  - 3 digits: R5, R10, R20, R40, R80

This package provides them as integer numbers to avoid floating point problems.

e.g.)
* E3: 10, 22, 47
* E6: 10, 15, 22, 33, 47, 68
* E48: 100, 105, ..., 909, 953 (48 numbers)
* R5: 100, 160, 250, 400, 630
* R80: 100, 103, ... , 950, 975 (80 numbers)


## Installation

```bash
pip install git+git://github.com/konayuki002/preferred_numbers.git
```

## Example

```python
from preferred_numbers import PreferredNumbers

print(PreferredNumbers.values_e(3))

# Output
# [10, 22, 47]

print(PreferredNumbers.value_r(5, 4))

# Output
# 630
```

### Test

First, install the package in editable mode.
```bash  
pip install -e .
```

Then, run the tests.
```bash
python -m unittest
```

### Build
  
```bash
python -m build
```