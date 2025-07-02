num=int(input("Enter three digit no :"))

a=num % 10
num=num // 10
c=num % 10
d=num // 10
sum = a+c+d
print("total sum is :",sum)
