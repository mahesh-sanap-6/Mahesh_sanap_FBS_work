amount=int(input("Enter the amount :"))

n500= amount // 500
r_amount=amount % 500

n200=r_amount//200
r_amount=r_amount%200

n100=r_amount//100
r_amount=r_amount%100

n50=r_amount//50
r_amount=r_amount%50

n20=r_amount//20
r_amount=r_amount%20

n10=r_amount//10
r_amount=r_amount%10
print("total amount to pay",amount)
print("notes of 500 :",n500)
print("notes of 200 :",n200)
print("notes of 100 :",n100)
print("notes of 50 :",n50)
print("notes of 20 :",n20)
print("notes of 10 :",n10)