# def threeSum( nums: list[int]) -> list[list[int]]:
#     def twoSum(nums: list[int], target: int) -> list[int]:
#         for i in range(0, len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return ([i, j])
            
#     for i in range(0, len(nums)):
#         remain = 0 - nums[i]
#         temp = list(nums)
#         temp.remove(nums[i])
#         indeces = twoSum(temp, -remain)
#         if indeces != None and (nums[i] + temp[indeces[0]] + temp[indeces[1]] == 0):
#             print(nums[i], temp[indeces[0]], temp[indeces[1]])

# #WIP
        

# threeSum([-1,0,1,2,-1,-4])