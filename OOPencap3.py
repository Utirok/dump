import random


class Bunker:

    def __init__(self, code):
        self.code = code
        self.new_code_delta = random.randint(-100, 100)
        self._password = ''

    def set_password(self):
        print('set the secret password...')
        self._password = input()

    def __private(self):
        new_code = self.code + self.new_code_delta
        print('new secret code is ' + str(new_code))

    def public(self):
        print('the old code is ' + str(self.code))
        password = input('enter the secret password...')
        if password == self._password:
            self.__private()
        else:
            print('incorrect input, kill the spy...')
            quit()


spy = Bunker(543234234)
spy.set_password()
spy.public()
