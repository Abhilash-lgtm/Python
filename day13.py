## L-90
# n=5
# for r in range (1, n+1):
#  print(r*"*")
# for r in range (n,-2,-1):
#   print (r*"*")


##trianle
# n=5
# for r in range (1, n+1):
#  print((n-r)*' '+(r)*"* ")
# for r in range (n-1,0,-1):
#  print((n-r)*' '+(r)*"* ")


# # #holo square
# n = 5
# for r in range (n):
#     for c in range (n):
#         if r == 0  or  c==n-1 or c==0  or r==n-1 :
#             print('*',end=' ')
#         else:
#             print(' ',end=" ")
#     print ()


# # Star
# n = 5
# for r in range (n):
#     for c in range (n):
#         if r == n//2 or c==n//2 or c==r or r==n-c-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=" ")
#     print ()

# holo star
n=5
for r in range (n):
    if r == 0:
        print(2*(n-1)*'*')
    else :
        print((n-r)*'*' + (2*(r-1))* ' ' + (n-r)*'*')
# print ()
# reverse holo star
for r in range (n-1,0,-1):
    if r == n:
        print(2*(n-1)*'*')
    else :
        print((n-r)*'*' + (2*(r-1))* ' ' + (n-r)*'*')
print ()

