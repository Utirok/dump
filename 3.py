stroka = str(input())
stoka = stroka.replace(" ", '')
stroka = stroka.lower()
x = stroka[:(len(stroka) + 1) // 2]
x = x[::-1]
y = stroka[len(stroka)//2:]
if x == y:
    print('Палиндром')
else:
    print("Не палиндром")
