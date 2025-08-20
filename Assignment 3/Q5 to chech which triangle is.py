side1=int(input("Enter side1: "))
side2=int(input("Enter side2: "))
side3=int(input("Enter side3: "))

if side1 == side2 and side2 == side3:
    print("The triangle is Equilitral (all side are equal)")
elif side1 == side2 or side2 == side3 or side1 == side3:    
    print("The triangle is isosceles (two sides are equal)")
else:
    print("The triangle is scalene (All sides are different)")    