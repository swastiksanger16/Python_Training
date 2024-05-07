"""2. Write a program  Display Fibonacci series up to 10 terms using recursion"""

def fibonnaci(n,num1,num2):
    if n<3:
        return
    fib_num=num1+num2
    num1=num2
    num2=fib_num
    print(fib_num,end=" ")
    fibonnaci(n-1,num1,num2)
    
num=int(input("Enter Number Of Occurance: "))

if(num<1):
    print("INVALID")
elif(num==1):
    print("0",end=" ")
elif(num==2):
    print("0 1",end=" ")
else:
    print("0 1",end=" ")
    fibonnaci(num,0,1)

        