def factorial(str,stop):
    for i in range(str,stop+1):
        if (i%2 == 1):
             return 1
        else:
            return i*factorial(i-1)
    
str=int(input("Enter the starting number: "))
stop =int(input("Enter ending number"))
x=factorial(str,stop) 
print(x)   