#encoding:utf -8

import random

num1=input("请输入一个0到100内的数字：")
num1=int(num1)
num2=random.randint(0,100)
i=1

while i<5:
    if num1==num2:
        print("恭喜你，答对了")
        break
    elif num1>num2:
        print("猜大了")
    elif num1<num2:
        print("猜小了")

    num1=input("请输入一个0到100内的数字：")
    num1=int(num1)
    i+=1
else:
    print('太笨了，下次再来吧')
   
