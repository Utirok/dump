class BankAccount:
    def __init__(self, name):
        self.name = name
        self._balance = 0
        self._password = ''

    def add_money(self, money):
        self._balance += money

    def set_balance(self, money):
        self._balance = money

    def set_password(self, password):
        self._password = password

    def get_balance(self):
        if self._password == '':
            print('set a password...')
        else:
            sign = input('input a password...')
            if sign == self._password:
                print('you have ' + str(self._balance))
            else:
                print('incorrect password...')


who = BankAccount('Utirok')
who.set_balance(1000)
who.add_money(2000)
who.get_balance()
who.set_password(input())
who.get_balance()
