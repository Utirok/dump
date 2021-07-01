class Figures:
    name = "Figure"

    def __init__(self, size):
        self.color = 'white'
        self.size = size

    def change_color(self, new_color):
        self.color = new_color

    def change_size(self, new_size):
        self.size = new_size

    def info(self):
        if self.name in {"Oval", 'Square'}:
            pass
        else:
            print('color: ' + str(self.color) + ' size: ' + str(self.size))


class Oval(Figures):
    name = 'Oval'

    def __init__(self, size):
        super().__init__(size)

    def info(self):
        print('figure: ' + str(self.name) + '; color: ' + str(self.color) + '; size: ' + str(self.size))


class Square(Figures):
    name = 'Square'

    def __init__(self, size):
        super().__init__(size)

    def info(self):
        print('figure: ' + str(self.name) + '; color: ' + str(self.color) + '; size: ' + str(self.size))


rectangle = Figures(43)
rectangle.change_color('green')
rectangle.info()
oval = Oval(123)
oval.info()
oval.change_color('orange')
oval.change_size(3)
oval.info()