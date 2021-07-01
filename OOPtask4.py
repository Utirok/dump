class Company:

    def sell(self, customer, tickets):
        if [customer.place] not in tickets.sold_tickets:
            tickets.sold_tickets.append([customer.place])
            tickets.number -= 1
            print('place - ' + str([customer.place]))
        else:
            print('incorrect')


class Customer:
    def __init__(self, place):
        self.place = place


class Tickets:
    def __init__(self):
        self.number = 1000
        self.sold_tickets = []

    def print_number(self):
        print(str(self.number) + ' tickets left')


ticket = Tickets()
customer_1 = Customer(56)
customer_2 = Customer(2)
customer_3 = Customer(1234)
customer_4 = Customer(2)
company = Company()
company.sell(customer_1, ticket)
company.sell(customer_2, ticket)
company.sell(customer_3, ticket)
customer_2 = Customer(52)
company.sell(customer_2, ticket)
ticket.print_number()
