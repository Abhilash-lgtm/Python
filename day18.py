#List Comprehension
#for
a = []
for x in range(1, 11):
    a.append(x)
print(a)
#create same list with comprehension


#for-if
a = []
for x in range(1,11):
    if x % 2 == 0:
        a.append(x) 
print(a)
#create same list with comprehension

#for-if-for-if 
a = []
for x in range(1,5):
    if x % 2 == 0:
        for y in range(1,4):
            if x + y == 5:
                a.append((x,y))
print(a)
#create same list with comprehension

#set comprehension
l = [3,4,3,5,6,7,6]
#create list, set, dict comrehension with above list

#function
def numbers():
    return 1 
    return 2 
n = numbers()
print(n)
print(type(n))

#generators
def numbers():
    yield 1 
    yield 2 
    yield 3 
    yield 4 
n = numbers() 
print(n)
print(type(n))
print(next(n))
print(next(n))
print(n.__next__())
print(n.__next__())
print(next(n)) 

def evennumbers():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x 
n = evennumbers()
print(next(n))
print(n.__next__())
for x in n:
    print(x)


#write generator to generate odd numbers
#write generator to generate even numbers
#write generator to generate prime numbers
