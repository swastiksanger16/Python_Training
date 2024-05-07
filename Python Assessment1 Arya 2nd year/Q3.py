"""3. Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690"""


def printSeries(n):
    num=2
    sum=0
    print("The Series is: ")
    for x in range(1,n+1):
        print(num,end=" ")
        sum+=num
        temp=2
        num=(num*10)+temp
        temp=num
    print("\n\nSum of Series: ",sum)
printSeries(5)