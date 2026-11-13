
'''
Scenario: Supermarket Discount System
A supermarket gives discounts based on the customer's purchase amount:
If purchase amount is ₹5000 or more → 20% discount
If purchase amount is ₹3000 or more → 10% discount
If purchase amount is ₹1000 or more → 5% discount
Otherwise → No discount
'''

n = int(input("Enter the Amount :-"))
if n >= 5000:
    n = n - (n * 20/100)
    print(n, "= 20% discount")
elif n >= 3000:
    n = n - (n * 10/100)
    print(n, "= 10% discount")
elif n >= 1000:
    n = n - (n * 5/100)
    print(n, "= 5% discount")
else:
    print(n, "= No discount")

'''
🎯 Student Task
Scenario: An online shopping website calculates delivery charges:
Order amount ≥ ₹2000 → Free delivery
Order amount ≥ ₹1000 → ₹50 delivery charge
Otherwise → ₹100 delivery charge
 write a Python program using if-elif-else to calculate the final amount including delivery charges.
 '''
n = int(input("Enter the  Amount :-"))
if n >= 2000:
    print("total charges:",n, "Free delivery")
elif n >=1000:
    n = n+50
    print("total charges:",n, " + 50 for delivery charges")
else:
    n = n +100
    print("total charges:",n, " + 100 for delivery charges")

'''
Real-Time Scenario: Electricity Bill Calculation
An electricity company calculates the bill based on the number of units consumed:
Units Consumed Rate per Unit
0-100.                   ₹2
101-200.                 ₹3
201-300                  ₹5
Above 300.               ₹7
Write a Python program using if-elif-else to:
Take the number of units consumed as input.
Calculate the electricity bill based on the applicable rate.
Print the total bill amount.
'''

n = int (input("Enter the number of units consumed: "))
if n <=100:
    n =  n*2
    print("Total bill amount: ₹",n)
elif n <=200:
    n = n*3
    print("Total bill amount: ₹",n)
elif n<300:
    n = n*5
    print("Total bill amount: ₹",n)
else:
    n = n*7
    print("Total bill amount: ₹",n)