def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    test = []
    for i in range(0, len(matrix)):
        test += matrix[i]
    return target in test



print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))