#Write a program to enter P, T, R and calculate Compound Interest.
pr=int(input("Enter the princepal amount:"))
years=int(input("Enter total no of years:"))
rate=float(input("Enter rate:"))
time=int(input("enter time in yeras :"))

compound_intrest=pr*(1+(rate/years))**(years*time)
print("intrest is:",compound_intrest)