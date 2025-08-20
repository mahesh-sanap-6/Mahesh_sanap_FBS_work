amount=int(input("enter amount: "))
#500
n500=amount//500
r_amount=amount%500

#200 
n200=r_amount//200
r_amount=r_amount%200

#100
n100=r_amount//100
r_amount=r_amount%100

#50
n50=r_amount//50
r_amount=r_amount%50

#20
n20=r_amount//20
r_amount=r_amount%20

#10
n10=r_amount//10
r_amount=r_amount%10
print("notes amount: ",amount)
print("total notes of 500: ",n500)
print("total notes of 200: ",n200)
print("total notes of 100: ",n100)
print("total notes of 50: ",n50)
print("total notes of 20: ",n20)
print("total notes of 10: ",n10)
