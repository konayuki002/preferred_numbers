# Preferred numbers from E-series

This is the provider of the preferred numbers from the E-series.

## E-series
e.g.:
E3 = [10, 22, 47]
E6 = [10, 15, 22, 33, 47, 68]

## Installation

```bash
pip install git+git://github.com/konayuki002/preferred-numbers/preferred_numbers.git
```

## Example

```python
from preferred_numbers import PreferredNumbers

print(PreferredNumbers.values(3))

# Output
# [10, 22, 47]

print(PreferredNumbers.value(6, 3))

# Output
# 33
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