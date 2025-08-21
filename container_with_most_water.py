def maxArea(height: list[int]) -> int:
    front = 0
    back = len(height)-1
    biggest = 0
    while front != back:
        line_1, line_2 = height[front], height[back]
        area = (min(line_1, line_2) * (back-front))
        if area > biggest:
            biggest = area
        if line_1 < line_2:
            front += 1
        else:
            back -= 1
    return biggest
            
print(maxArea([1,8,6,2,5,4,8,3,7]))