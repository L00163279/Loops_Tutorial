# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................

#count odd numbers and even number
#read a maximum number
#check odd or even with condition
#count the number


if __name__ == '__main__':
    even_count = 0
    odd_count = 0
    #num=0
    max = int(input("enter the maximum number: "))
    for i in range(max):
        if i % 2 == 0:
            print("even : {}".format(i))
            even_count += 1

        else:
            odd_count += 1
            print("odd : {}".format(i))


    print("count of even number", even_count)
    print("count of odd number", odd_count)