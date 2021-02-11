x = int(input())
sum = 0


while x>0:
    ost = x%10
    sum=sum + ost
    x=x//10
print ('Сумма: ', sum)
