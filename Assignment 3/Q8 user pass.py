import random
user_id=input("Enter user_id: ")
pass1=input("Enter password: ")

user_id="fbs"
pass1="fbs123"

if(user_id=="fbs" and pass1=="fbs123"):
    captcha= random.randint(1000,9999)
    print("captcha: ",captcha)
    input=int(input("Enter the captcha: "))
    if(input==captcha):
        print(" Successfully login")
    else:
        print("Wrong captcha")    
else:
    print("Wrong user_id or password")        