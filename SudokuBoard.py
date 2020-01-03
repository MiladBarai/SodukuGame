class SudokuBoard:
    def __init__(self, preset_squares):
        """
        initializes the SudokuBoard
        :param preset_squares: list of tuples (x, y, val) of the preset values for the sudoku board
        """

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

    def display_board(self):
        """
        prints board
        :return:
        """

    def input_val(self, square, val):
        """
        Tries to input value into the square
        :param square: tuple (x, y)
        :param val: int value to input in square
        :return: boolean, true if val set, false if not
        """

    def remove_val(self, square, val):
        """
        Tries to remove value from the square
        :param square: tuple (x, y)
        :param val: int value to input in square
        :return: boolean, true if val was removed, false if not
        """