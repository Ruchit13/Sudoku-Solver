from pprint import pprint


def find_next_empty(puzzle):
    # Finds the next row,col in the puzzle that is not filled yet -->rep with -1
    # Returns row, col tuple (or (none, none) if there is none)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None


def is_valid(puzzle, guess, row, col):
    # figures if your guess is right or wrong
    # return True if its correct else False
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals=[]
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False

    # and then for the square 3x3
    # iterate over the 3 values in the row/column

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    # if the control comes here, then we have given the right value
    return True



def solve_sudoku(puzzle):
    # Solves Suduko using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our suduko puzzle
    # return whether the solution exists
    # mutates puzzle to be solution

    # step 1: choose somewhere in the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # Step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True

    # step 2: if there is a place to put a number, then we make a guess between 1 to 9
    for guess in range(1, 10):
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1 : if the guess is valid, place it on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

        # step 5: if not valid OR if our guess does not solve the puzzle,we need to backtrack
        puzzle[row][col] = -1

    # step 6: if none of the numbers we try work, then its UNSOLVABLE!
    return False

if __name__ == '__main__':
    example_board = [
        [3,   9, -1,   -1, 5, -1,    -1,-1, -1],
        [-1, -1, -1,    2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,    7, 1, 9,     -1, 8, -1],

        [-1, 5, -1,    -1, 6, 8,     -1, -1, -1],
        [2, -1, 6,     -1, -1, 3,    -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,     1, -1, 5,    -1, 4, -1],
        [1, -1, 9,    -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)




