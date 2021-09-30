# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................
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


    print("count of even number", even_count)
    print("count of odd number", odd_count)