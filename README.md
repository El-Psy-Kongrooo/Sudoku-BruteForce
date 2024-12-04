Sudoku Solver with Brute-Force Approach
This Python script solves a given Sudoku puzzle using a brute-force backtracking algorithm. It can be run as a standalone script with a default puzzle board or with a custom board provided via command-line arguments.

Usage
Default Board: If no input is provided, the script will solve a predefined Sudoku puzzle.

python3 BFSudoku.py

Custom Board: To solve a custom puzzle, pass nine strings as command-line arguments, each representing a row in the Sudoku grid. Each string should contain exactly 9 characters, with numbers 1-9 for filled cells and a . to denote empty cells.

python3 BFSudoku.py 
```plaintext
"........." 
"5.3.67..." 
"9..3421.." 
".....4..." 
"..1...72." 
"..2.1...." 
".3......9" 
".8.1..2.." 
"...75.8.6"
```

Input Validation
The script includes validation checks to ensure the input is well-formed:

Row Count: The input must contain exactly 9 rows.
Row Length: Each row must consist of exactly 9 characters.
Valid Characters: Only digits 1-9 and the character . are allowed. The dot (.) denotes an empty cell.
If the input does not meet these requirements, the script will print an error message and exit.

Algorithm
The brute-force solver applies a recursive backtracking approach to fill empty cells. It first fills cells with obvious moves (cells with only one possible value), then proceeds to guess values for other cells, backtracking if a guess leads to an invalid state. This approach guarantees a solution if one exists.

Example Output
The script displays the Sudoku board with dividers between the 3x3 sub-grids, providing a clear visual of the puzzle’s progress as it is being solved.

