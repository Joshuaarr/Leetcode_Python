class Solution:
    def minFlips(self, target: str) -> int:
        res = 0
        prev = '0'
        for i in range(len(target)):
            if target[i] != prev:
                res += 1
            prev = target[i]

        return res
        