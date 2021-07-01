class Box:
    def __init__(self, figures):
        self.figures = figures

    def add(self, figure):
        self.figures.append(figure)

    def info(self):
        print('figures: ' + str(self.figures))


class Figure:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return str(self.type)


figure1 = Figure('square')
figure2 = Figure('circle')
figure3 = Figure('triangle')
figure4 = Figure('rectangle')

box_1 = Box([])
box_2 = Box([])

box_1.add(figure1)
box_1.add(figure2)
box_1.info()
