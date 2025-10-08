arr = [1, 0, 0, 2, 3, 4, 0, 1]
n = len(arr)
write_index = 0

# First, move all non-zero elements to the front
for i in range(n):
    if arr[i] != 0: # if move zeroes to first change ==
        arr[write_index] = arr[i]
        write_index += 1

# Fill remaining positions with zeros
for i in range(write_index, n):
    arr[i] = 0

print(arr)  # [1, 2, 3, 4, 1, 0, 0, 0]


#def move_zeros_swap(arr):
#    n = len(arr)
#    pos = 0
#    
#    for i in range(n):
#        if arr[i] != 0:
#            arr[pos], arr[i] = arr[i], arr[pos]
#            pos += 1
#    
#    return arr
#
#arr = [1, 0, 0, 2, 3, 4, 0, 1]
#print(move_zeros_swap(arr))  # [1, 2, 3, 4, 1, 0, 0, 0]
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#def move_zeros_pythonic(arr):
#    return [x for x in arr if x != 0] + [0] * arr.count(0)
#
#arr = [1, 0, 0, 2, 3, 4, 0, 1]
#print(move_zeros_pythonic(arr))  # [1, 2, 3, 4, 1, 0, 0, 0]