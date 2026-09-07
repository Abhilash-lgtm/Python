# #if
# n = 1
# if n == 1: 
#     print(1)  #1
# print(2)
# print()

# #if-else 
# n = 10
# if n == 10:
#     print(1)    #1
# else:
#     print(2)
# print(3)
# print() 
# if n == 20:
#     print(1)   
# else:
#     print(2)        #2
# print(3)
# print()         #2

# #if-elif-else
# n = 3
# if n == 1:
#     print(1)
# elif n == 2:
#     print(2)
# elif n == 3:
#     print(3)            #3
# else:
#     print(10)
# print(11)
# print()                 #3
# n = 5
# if n == 1:
#     print(1)
# elif n == 2:
#     print(2)
# elif n == 3:
#     print(3)
# else:
#     print(10)           #10
# print(11)               #11

# #nested-if
# ch = 'A'  #one char
# if ch.isalpha():
#     if 65 <= ord(ch) <= 90:    
#         print('upper case letter')      # upper case letter to
#     elif 97 <= ord(ch) <= 122:
#         print('lower case letter')
# else:
#     print('not an letter')
# print(1)                                # upper case letter to

# #match case 
# day = 5 
# match day:
#     case 1: 
#         print('Sunday')
#     case 2:
#         print('Monday')
#     case 3:
#         print('Tuesday')
#     case 4:
#         print('Wednesday')
#     case 5:
#         print('Thursday')   #thusday
#     case 6:
#         print('Friday') 
#     case 7:
#         print('Saturday')           #thusday

# age = int(input())
# if age >= 18:
#     print('eligible for voting')  #eligible for voting
# else:
#     print('not eligible for voting')

gread = int(input("enter your greade ="))
if gread >= 90:
    print ("gread 'A'")
elif gread >= 75:
    print("gread 'B'")
elif gread >= 60:
    print("gread 'C'")
elif gread >= 50:
    print("gread 'D'")
elif gread >=35:
    print("pass")
else :
    print("fail")