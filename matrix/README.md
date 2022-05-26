MATRIX
=======

- Seed a matrix 5x5 with integers (-999 to 999)
- Find a horizontal/vertical sequence

usage:

`python3 matrix.py`

```
from matrix import Matrix
matrix = Matrix().seed_matrix()
Matrix().print_matrix(matrix)  # pretty print matrix
# find a horizontal/vertical sequence of consecutive numbers
sequence = matrix.find_sequence()
```
test:

`python3 test.py`

