angle1=int(input("Enter angle1: "))
angle2=int(input("Enter amgle2: "))
angle3=int(input("Enter angle3: "))

sum_of_angles = angle1 + angle2 +angle3
if sum_of_angles == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The triangle is valid")

else:
    print("Triangle is not valid")    