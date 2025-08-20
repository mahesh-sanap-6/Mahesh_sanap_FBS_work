units=float(input("Enter the units"))
bill=0

if(units<=50):
    bill=units*0.50
elif(units<=150):
    bill=50*0.50
    units=units-50
    bill+=100*0.75
elif(units<=250):
    bill=50*0.50
    bill+=100*0.75
    units=units-150
    bill+=100*1.20
else:
    bill=50*0.50
    bill+=100*0.75
    bill+=100*1.20
    
    units=units-250
    bill+=250*1.50

surchar=bill*0.20
total_bill = bill+surchar
print("total bill is: ",total_bill)                