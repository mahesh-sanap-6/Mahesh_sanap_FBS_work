# write a factorial to which we pass a parameter and print the factors of given number 
def factorial(num):
    factorial = []
    for i in range(1,num+1):
        if (num%i == 0):
            factorial.append(i)
    return factorial       
num=int(input("Enter the number: "))
ans=factorial(num)
print(ans)
