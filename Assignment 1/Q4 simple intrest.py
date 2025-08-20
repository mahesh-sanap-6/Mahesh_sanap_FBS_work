#Write a program to enter P, T, R and calculate simple Interest.
pr=int(input("Enter the princepal amount:"))
years=int(input("Enter total no of years:"))
rate=float(input("Enter rate:"))

intrest=(pr*years*rate)/100
print("intrest is:",intrest)