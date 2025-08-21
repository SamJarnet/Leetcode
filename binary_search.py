def search(nums: list[int], target: int) -> int:
    def split(arr, point_sum):
        if len(arr) == 0:
            return -1
        if len(arr) == 1:
            return point_sum if arr[0] == target else -1

        mid = len(arr) // 2

        if arr[mid] > target:
            return split(arr[:mid], point_sum)
        else:
            return split(arr[mid:], point_sum + mid)
    return split(nums, 0)

print(search([-5, 2, 0, 1, 2, 4, 5, 6, 7, 10], 7))