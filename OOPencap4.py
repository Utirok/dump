class Chess:
    def __init__(self):
        self.__x = 2
        self.__y = "C"
        self.__figure = "bishop"

    def set_x(self, x):
        if self.__figure in {"rook", "knight", "bishop", "queen", "king"}:
            if x in range(1, 8):
                self.__x = x
            else:
                print('Something is wrong')
        elif self.__figure == "pawn":
            if x in range(2, 7):
                self.__x = x
            else:
                print('Something is wrong')
        else:
            print('Something is wrong')

    def set_y(self, y):
        if y in {"A", "B", "C", "D", "E", "F", "G", "H"}:
            self.__y = y
        else:
            print('Something is wrong')

    def set_figure(self, figure):
        if figure in {"rook", "knight", "bishop", "queen", "king"}:
            self.__figure = figure
        elif figure == "pawn" and self.__x == 1 or self.__x == 8:
            print('Something is wrong')
        else:
            self.__figure = figure

    def get_situation(self):
        if self.__x != 0 and self.__y != "":
            print(f'There is a {self.__figure} on {self.__y}{self.__x}')
        else:
            print('Something is wrong')


sit = Chess()
sit.set_x(3)
sit.set_y("B")
sit.set_figure("rook")
sit.get_situation()

sit.set_x(1)
sit.set_y("B")
sit.set_figure("pawn") # pawn can't stand on the first or the last line

