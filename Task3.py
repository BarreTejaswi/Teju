while True:
    print("1 for addition")
    print("2 for substractio")
    print("3 for multiplication")
    print("4 for division")
    print("5 for floor division")
    ch=int(input("enter your choice"))
    print("enter two numbers")
    a=int(input(""))
    b=int(input(""))
    if ch==1:
        sum=a+b
        print("addition is",sum)
    elif ch==2:
        dif=a-b
        print("substraction is",dif)
    elif ch==3:
        mul=a*b
        print("multiplication is",mul)
    elif ch==4:
        div=a%b
        print("division is",div)
    elif ch==5:
        flo=a//b
        print("floor division is",flo)
    while True:
        z=input("do you want to continue[Y/y]")
        if z=="Y" or z=="y":
            break
        else:
            exit(0)
