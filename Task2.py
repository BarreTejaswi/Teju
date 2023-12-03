def que1():
    print("1.what is the capital of france")
    print("a.new york")
    print("b.paris")
    print("c.london")   
    print("d.dublin") 
    que=input("")   
    if que=="b":
        print("correct!")
        return 1
def que2():
    print("\n2.which avenger is green in color")
    print("a.spider man")
    print("b.Thor")
    print("c.Hulk")   
    print("d.captain america") 
    que=input("")   
    if que=="c":
        print("correct!")
        return 1
def que3():
    print("\n3.The iphone was created by")
    print("a.Apple")
    print("b.Intel")
    print("c.Amazon")   
    print("d.Microsoft") 
    que=input("")   
    if que=="a":
        print("correct!")
        return 1
def que4():
    print("\n4.how many harry potter books are there")
    print("a.1")
    print("b.4")
    print("c.6")   
    print("d.7") 
    que=input("")   
    if que=="d":
        print("correct!")
        return 1
x=que1()
y=que2()
w=que3()
z=que4()
count=0
if x==1:
    count=count+1
else:
    pass
if y==1:
    count=count+1
else:
    pass
if w==1:
    count=count+1
else:
    pass
if z==1:
    count=count+1
else:
    pass
print("your score is",count)
