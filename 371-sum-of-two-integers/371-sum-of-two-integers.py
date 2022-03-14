class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask:
            tmp = (a & b) << 1
            a = (a ^ b) 
            b = tmp 
        return (a & mask) if b > mask else a