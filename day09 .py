#  LINK: https://www.hackerrank.com/challenges/py-if-else/problem

# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print("Weird")
    elif 2 <=n<= 5:
        print ("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else :
        print ("Not Weird")


#LINK: https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    return False
year = int(input())
print(is_leap(year))