# Brute Force
class Solution:
    def countBits(self, n: int) -> List[int]:
        num, res = 0, []
        while num <= n:
            if num == 0:
                res.append(0)
            else:
                i, count = num, 0
                while i:
                    count += i % 2
                    i = i >> 1
                res.append(count)
            num += 1
        return res