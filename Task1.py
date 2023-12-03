import random   
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="1234567890"
character="!@~#$%^&*()"
x=lower+upper+digits+character
while True:
    p=int(input("enter the length of the password "))
    print("your password is ",end="")
    for i in range(p):
        password=random.choice(x)
        print(password,end="")
    while True:
        ch=input("\ndo you want to continue to generate password[Y/N]")
        if ch=='Y' or ch=='N':
            break
        else:
            exit(0)
