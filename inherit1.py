class Table:

    def __init__(self, length, width, edges):
        self.length = length
        self.width = width
        self.edges = edges


class Square_objects(Table):
    def check(self, n):
        if n == 0:
            print("it's a round table")
        else:
            print("it's not a round table")

    def cut_edges(self, n):
        if n == 0:
            n += 2
        else:
            n += 1
        print('now there are ' + str(n) + ' edges')

    def square(self, height, width):
        return (height * width)


#class Square_objects(Table):
#    def __init__(self, length, width, state):
#        super().__init__(length, width)
#       self.state = state
#       self.some_state = [self.state]



class Round_objects(Table):
    def __init__(self, length, width, thing):
        super().__init__(length, width, 0)
        self.thing = thing
        self.some_things = [self.thing]

    def put(self, thing):
        self.some_things.append(thing)

    def look(self):
        print('things on the table: ' + str(self.some_things))


table1 = Round_objects(5, 10, 'apple')
table1.look()
table1.put('book')
table1.put('bottle')
table1.look()