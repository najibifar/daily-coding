def func(Tuple):
    return Tuple
print(func((1, 2, 3)) * 2)


List = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

for i in range(0,4):
    print(List[i][1], end="/")