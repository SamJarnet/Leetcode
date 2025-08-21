def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    sorted_arr = ((sorted(nums1+nums2)))
    length = len(sorted_arr)
    if length % 2 == 0:
        print(length//2)
        return (sorted_arr[(length//2)-1]+sorted_arr[length//2])/2
    else:
        return (sorted_arr[length//2])

print(findMedianSortedArrays([1,2], [3,4]))