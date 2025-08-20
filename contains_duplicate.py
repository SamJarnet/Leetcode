def containsDuplicate(nums: list[int]) -> bool:
    
    if len(set(nums)) < len(nums):
        return True
    return False


print(containsDuplicate( [1,2,3,1]))