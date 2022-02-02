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

Would be input as:

```
..7......6.4.....3....54..2....4....9.......5385..2........378.49.71....1....89..
```

## Algorithm

This solver uses a simple algorithm known as "Backtracking". The steps are as follows:

1. Find an unfilled square
2. Try digits 1-9 in that square
3. Check if that digit is valid
4. If the digit is valid, move on to the next square  
   Else, reset the square and 'backtrack'
