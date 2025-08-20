a1=int(input("Enter the age: "))
a2=int(input("Enter the age: "))
a3=int(input("Enter the age: "))
a4=int(input("Enter the age: "))
a5=int(input("Enter the age: "))
amt=100
fair=0
if(a1<12):
    fair+= amt-amt*0.3
elif(a1>59):
    
    fair=amt*0.5    
#else:
   # fair=amt
if(a2<12):
    fair+= amt-amt*0.3
elif(a2>59):
    fair=amt*0.5    
#else:
   # fair=amt
if(a3<12):
    fair+= amt-amt*0.3
elif(a3>59):
    fair=amt*0.5    
#else:
   # fair=amt
if(a4<12):
    fair+= amt-amt*0.3
elif(a4>59):
    fair=amt*0.5    
#else:
  #  fair=amt
if(a5<12):
    fair+= amt-amt*0.3
elif(a5>59):
    fair=amt*0.5    
else:
    fair=amt
print("Total of all ticket: ",fair)    






