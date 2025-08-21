class Solution:
    def __init__(self):
        self.cache = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        for i in range(3, n+1):
            steps = (self.cache[i-1] + self.cache[i-2])
            self.cache.update({i:steps})
        return self.cache[n]
solution = Solution()
print(solution.climbStairs(10))