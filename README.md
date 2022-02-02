# Sudoku Solver

## Input

This program takes a sudoku board as all 9 rows packed together.
For example, a sudoku board that looks like this:

```
+-----------------------+
| . . 7 | . . . | . . . |
| 6 . 4 | . . . | . . 3 |
| . . . | . 5 4 | . . 2 |
| - - - + - - - + - - - |
| . . . | . 4 . | . . . |
| 9 . . | . . . | . . 5 |
| 3 8 5 | . . 2 | . . . |
| - - - + - - - + - - - |
| . . . | . . 3 | 7 8 . |
| 4 9 . | 7 1 . | . . . |
| 1 . . | . . 8 | 9 . . |
+-----------------------+
```

Would be input as the string:

```
"..7......6.4.....3....54..2....4....9.......5385..2........378.49.71....1....89.."
```

## Algorithm

This solver uses a simple algorithm known as "Backtracking".
This is a brute force approach that tests a value, and moves on.
Once the value is no longer valid, it backtracks and tries a new value.
