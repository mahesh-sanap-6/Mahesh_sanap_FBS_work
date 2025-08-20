num=int(input("Enter the number: "))
copy=num

a=num %10
num=num//10
b=num%10
revers=(a*10)+b
c=num//10
revers=(revers*10)+c
print("revers",revers)
if(copy == revers):
    print("number is palindrom")
else:
    print("number is not palindrom")    