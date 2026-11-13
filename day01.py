arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print (arr)     #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print (arr[0][0]) #1
# print (arr[0][1]) #2
# print (arr[0][2]) #3
# print (arr[1][0]) #4
# print (arr[1][1]) #5
# print (arr[1][2]) #6
# print (arr[2][0]) #7
# print (arr[2][1]) #8
# print (arr[2][2]) #9

for i in range (len(arr)):
    for j in range (len(arr[i])):
        print (arr[j][i], end =" ")
    print()
