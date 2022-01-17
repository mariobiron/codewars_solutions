# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]

def prt_block(block,sidelen):
    retlst = []
    total = sidelen * sidelen
    running_count = 0
    for j in range(0,sidelen):
        for i in range(0,sidelen-j-j):
            running_count+=1
            if running_count <= total:
                retlst.append(block[j][i+j])
        for i in range(1,sidelen-j-j):
            running_count += 1
            if running_count <= total:
                retlst.append(block[i+j][sidelen-1-j])
        for i in range(sidelen-1-j,j,-1):
            running_count += 1
            if running_count <= total:
                retlst.append(block[sidelen-1-j][i-1])
        for i in range(sidelen-2-j,j,-1):
            running_count += 1
            if running_count <= total:
                retlst.append(block[i][j])
    return retlst

def snail(snail_map):
    retlist = []
    if len(snail_map) > 1:
        retlist = (prt_block(snail_map,len(snail_map[1])))
    else:
        retlist = snail_map[0]
    return(retlist)

array = [[]]
expected = []
print(snail(array)) #), expected)

array = [[1]]
expected = [1]
print(snail(array)) #), expected)

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(snail(array)) #, expected)

array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(snail(array)) #, expected)

array = [[1,2,3,4,5],
         [16,17,18,19,6],
         [15,24,25,20,7],
         [14,23,22,21,8],
         [13,12,11,10,9]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(snail(array)) #, expected)

array = [[1,2,3,4,5,6],
         [20,21,22,23,24,7],
         [19,32,33,34,25,8],
         [18,31,36,35,26,9],
         [17,30,29,28,27,10],
         [16,15,14,13,12,11]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(snail(array)) #, expected)

# def snail(array):
#     ret = []
#     if array and array[0]:
#         size = len(array)
#         for n in xrange((size + 1) // 2):
#             for x in xrange(n, size - n):
#                 ret.append(array[n][x])
#             for y in xrange(1 + n, size - n):
#                 ret.append(array[y][-1 - n])
#             for x in xrange(2 + n, size - n + 1):
#                 ret.append(array[-1 - n][-x])
#             for y in xrange(2 + n, size - n):
#                 ret.append(array[-y][n])
#     return ret

# import numpy as np
#
# def snail(array):
#     m = []
#     array = np.array(array)
#     while len(array) > 0:
#         m += array[0].tolist()
#         array = np.rot90(array[1:])
#     return m

# # my implementation/explanation of the solution by foxxyz
# def snail(array):
#   if array:
#     # force to list because zip returns a list of tuples
#     top_row = list(array[0])
#     # rotate the array by switching remaining rows & columns with zip
#     # the * expands the remaining rows so they can be matched by column
#     rotated_array = zip(*array[1:])
#     # then reverse rows to make the formerly last column the next top row
#     rotated_array = rotated_array[::-1]
#     return top_row + snail(rotated_array)
#   else:
#     return []

# def snail(array):
#     out = []
#     while len(array):
#         out += array.pop(0)
#         array = list(zip(*array))[::-1] # Rotate
#     return out

# def snail(array):
#     next_dir = {"right": "down", "down":"left", "left":"up", "up":"right"}
#     dir = "right"
#     snail = []
#     while array:
#         if dir == "right":
#             snail.extend(array.pop(0))
#         elif dir == "down":
#             snail.extend([x.pop(-1) for x in array])
#         elif dir == "left":
#             snail.extend(list(reversed(array.pop(-1))))
#         elif dir == "up":
#             snail.extend([x.pop(0) for x in reversed(array)])
#         dir = next_dir[dir]
#     return snail 