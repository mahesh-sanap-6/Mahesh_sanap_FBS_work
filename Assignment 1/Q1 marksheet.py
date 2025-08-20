# Write a program to calculate the percentage of student based on marks of any 5 subject

mat=int(input("Enter marks of maths "))
mar=int(input("Enter marks of marath"))
phy=int(input("Enter marks of physic"))
eng=int(input("Enter marks of english"))
sci=int(input("Enter marks of science"))
 
totalmarks=(mat+mar+phy+eng+sci)
max=500
percentage=(totalmarks/max)*100
print("percentage",percentage)