"""2. Write a program  Display Fibonacci series up to 10 terms using recursion"""

def Fibonacci(num):
    num1=0
    num2=1
    print(num1,"\t")
    print(num2,"\t")
    while(num>2):  #num>2 as we have already printed two numbers 0 and 1
        num3=num1+num2
        print(num3,"\t")
        num1=num2
        num2=num3
        num-=1
        
Fibonacci(10)
        