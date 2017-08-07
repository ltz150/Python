#encoding:utf-8

num1=1
num2=1

while 10>num1>=num2:
    while num1>=num2:
        print(num2,'*',num1,'=',num1*num2,end='   ')
        num2+=1
    num1+=1
    num2=1
    print()
