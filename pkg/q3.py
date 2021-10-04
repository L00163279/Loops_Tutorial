# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................

#write a program that accepts a string and calculate number of digits, upper case letters and lower case letters

# split string into lists
# count digits
# check and count uppercase and lowercase letters

if __name__ == '__main__':
    string1 = input("Enter the string ")
    #print(string)
    name=list(string1.strip(" "))
    #print(name)
    count = 0
    upper_count = 0
    lower_count = 0
    for i in range(len(string1)):
        if (string1[i] >= 'A' and string1[i] <= 'Z'):
            upper_count += 1
        elif (string1[i] >= 'a' and string1[i] <= 'z'):
            lower_count += 1

        count += 1

    print("number of digits in the given string is {}".format(count))
    print("number of uppercase in the given string is {}".format(upper_count))
    print("number of lower case in the given string is {}".format(lower_count))






