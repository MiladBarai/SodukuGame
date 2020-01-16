from SudokuGame.SudokuBoard import SudokuBoard


def solve(sudoku_board):
    """
    Solves a sudoku board
    :param soduku_board: SudokuBoard Class
    :return: Boolean and Solution in the input soduku_board, if any
    """

    square = find_empty_square(sudoku_board)

    # Base case, return true if there are no more empty squares
    if square == (-1, -1):
        return True

    # Go Through all possible values from 1-9 for the square
    for i in range(1, 10):

        # Try to input value
        if sudoku_board.input_val(square, i):
            # Run the solver on the next square
            if solve(sudoku_board):
                return True
            # Error along the chain, then back up and change value
            else:
                sudoku_board.remove_val(square)

    # No more possible solutions for this chain
    return False




def find_empty_square(sudoku_board):
    """
    finds an empty square in the input sudoku_board
    :param sudoku_board: SudokuBoard Class
    :return: (int x, int y) position of empty square, (-1, -1) if no empty squares
    """
    for y in range(9):
        for x in range(9):
            if sudoku_board.get_value((x, y)) == 0:
                return (x, y)
    return (-1, -1)


if __name__ == '__main__':
    # Test case for the function
    preset = [(0, 0, 5), (1, 0, 3), (4, 0, 7), (0, 1, 6), (3, 1, 1), (4, 1, 9), (5, 1, 5), (1, 2, 9), (2, 2, 8),
              (7, 2, 6),
              (0, 3, 8), (4, 3, 6), (8, 3, 3), (0, 4, 4), (3, 4, 8), (5, 4, 3), (8, 4, 1), (0, 5, 7), (4, 5, 2),
              (8, 5, 6),
              (1, 6, 6), (6, 6, 2), (7, 6, 8), (3, 7, 4), (4, 7, 1), (5, 7, 9), (8, 7, 5), (4, 8, 8), (7, 8, 7),
              (8, 8, 9)]
    board = SudokuBoard(preset)
    solve(board)
    board.display_board()