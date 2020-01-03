class SudokuBoard:
    def __init__(self, preset_squares):
        """
        initializes the SudokuBoard
        :param preset_squares: list of tuples (x, y, val) of the preset values for the sudoku board
        """

        # Create initial board with zeroed squares
        self._sudoku_board = [[0 for i in range(9)] for j in range(9)]

        # Initialize a set for saving preset squares
        self._preset_square = set()
        for (x, y, val) in preset_squares:
            # Set the square
            self._sudoku_board[x][y] = val

            # Save the preset square in the set
            self._preset_square.add((x, y))
        print("Board initialized:\n")
        self.display_board()

    def validate_input(self, square, input):
        """
        Validates the input in the specific square
        :param square: tuple (x, y)
        :param input: int value to input in square
        :return: boolean, true if input possible, false if not
        """

    def validate_remove(self, square):
        """
        Validates if the value in the square can be removed or not,
        Not possible if square is set with preset values
        :param square: tuple (x, y)
        :return: boolean, true if input possible, false if not
        """
        (x, y) = square
        if square in self._preset_square or x not in range(0, 9) or y not in range(0, 9):
            return False
        return True

    def display_board(self):
        """
        prints board
        :return:
        """
        columns = len(self._sudoku_board)
        for y in range(columns):
            rows = len(self._sudoku_board[y])
            for x in range(rows):
                print_str = str(self._sudoku_board[x][y])
                end_with = ""

                if print_str == "0":
                    print_str = " "

                # if end of block add extra space
                if (x + 1) % 3 == 0:
                    end_with = "  "

                print("[" + print_str + "]", end=end_with)
            # Line break
            print()
            # if end of block add extra line seperator
            if (y + 1) % 3 == 0:
                print()

    def input_val(self, square, val):
        """
        Tries to input value into the square
        :param square: tuple (x, y)
        :param val: int value to input in square
        :return: boolean, true if val set, false if not
        """

    def remove_val(self, square):
        """
        Tries to remove value from the square
        :param square: tuple (x, y)
        :return: boolean, true if val was removed, false if not
        """
        (x, y) = square

        if x not in range(0, 9) or y not in range(0, 9):
            print("Remove out of range:", square)
            return False

        elif self.validate_remove(square):
            print("Removed val:", self._sudoku_board[x][y], "From:", square)
            self._sudoku_board[x][y] = 0
            return True

        else:
            print("Square:", square, "cannot be cleared, it is preset to:", self._sudoku_board[x][y])

        return False


if __name__ == '__main__':
    preset = [(0, 0, 5), (1, 0, 3), (4, 0, 7), (0, 1, 6), (3, 1, 1), (4, 1, 9), (5, 1, 5), (1, 2, 9), (2, 2, 8),
              (7, 2, 6),
              (0, 3, 8), (4, 3, 6), (8, 3, 3), (0, 4, 4), (3, 4, 8), (5, 4, 3), (8, 4, 1), (0, 5, 7), (4, 5, 2),
              (8, 5, 6),
              (1, 6, 6), (6, 6, 2), (7, 6, 8), (3, 7, 4), (4, 7, 1), (5, 7, 9), (8, 7, 5), (4, 8, 8), (7, 8, 7),
              (8, 8, 9)]
    board = SudokuBoard(preset)
    board.remove_val((0, 0))
