def longestConsecutive(nums: list[int]) -> int:
    if len(nums) == 0:
            return 0
    sorted_arr = sorted(list(set(nums)))
    count = [0]
    num = 0
    for i in range(1,len(sorted_arr)):
        if sorted_arr[i] -1 == sorted_arr[i-1]:
            count[num] += 1
        else:
            count.append(0)
            num+=1
    return max(count)+1
   


print(longestConsecutive([1,0,-1]

))