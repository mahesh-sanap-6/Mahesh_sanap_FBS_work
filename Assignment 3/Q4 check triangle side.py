side1=int(input("Enter side1: "))
side2=int(input("Enter side2: "))
side3=int(input("Enter side3: "))

if(side1+side2>side3) and (side2+side3>side1) and(side1+side3>side2):
    print("The triangle is valid")
else:
    print("Triangle is not valid")    