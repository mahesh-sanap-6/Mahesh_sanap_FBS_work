age=int(input("Enter your age: "))

gender=(input("Enter your gender: m/f: "))

if(gender=='m' and age>=21):
   print("You are eligible for marry")

elif(gender=='f' and age>=18):
      print("You are eligible for marry")
else:
     print("Wrong input")