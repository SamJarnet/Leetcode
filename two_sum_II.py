def twoSum(numbers: list[int], target: int) -> list[int]:
    num_set = set(numbers)
    for i in range(0, len(numbers)):
        remain = target-numbers[i]
        if remain in num_set:
            index = numbers.index(remain)
            print(index)
            if i == index:
                numbers.pop(i)
                index = numbers.index(remain)+1
            return [i+1, index+1]
        
    
print(twoSum([0,0,3,4], 0))