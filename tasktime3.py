import time

now = time.localtime()
today = time.strftime("%d.%m.%Y", now).split('.')
birthdate = input('date of birth: ').split('.')
days_number = 0
if int(birthdate[0]) in range(1, 31):
    if int(birthdate[1]) in range(1, 12):
        if int(birthdate[2]) in range(1, 2021):
            date = time.strftime("%d.%m.%Y", now)
            days = int(today[0]) - int(birthdate[0])
            month = (int(today[1]) - int(birthdate[1])) * 30
            years = (int(today[2]) - int(birthdate[2])) * 365
            days_number = years + month + days
else:
    print('incorrect date')
print(days_number)
