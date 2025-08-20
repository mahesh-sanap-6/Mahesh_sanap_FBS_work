marks1=int(input("Enter the marks of english: "))
marks2=int(input("Enter the marks of science: "))
marks3=int(input("Enter the marks of physic: "))
marks4=int(input("Enter the marks of chemestry: "))
marks5=int(input("Enter the marks maths: "))

total=marks1+marks2+marks3+marks4+marks5
percentage=(total/500)*100
print("percentage: ",percentage)


if(percentage>=80 and percentage<=100):
    print("First class with distinction")

elif(percentage>=70 and percentage<=80):
    print("First class")

elif(percentage>=60 and percentage<=70):
    print(" Higher Second class")

elif(percentage>=40 and percentage<=60):
    print("Second class") 

elif(percentage<40):
    print("Fail")

else:
    print("wrong input")          

   

