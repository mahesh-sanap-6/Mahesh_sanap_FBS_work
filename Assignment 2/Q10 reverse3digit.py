num=int(input("enter 3digit no: "))
a=num%10
num=num//10
b=num%10
revers=(a*10)+b
c=num//10
revers=(revers*10)+c
print("revers",revers)
