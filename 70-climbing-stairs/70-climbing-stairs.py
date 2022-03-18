class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        i = n - 1
        while i > 0:
            num = a
            a = num + b
            b = num
            i -= 1
        return a
            