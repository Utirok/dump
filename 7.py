stroka = input()


for i in stroka:
    x = stroka.find(i)
    z = stroka[:x] + stroka[x + 1:]
    a = z.find(i)
if a == -1:
    print('нет дубликатов')
else:
    print('есть дубликат')
