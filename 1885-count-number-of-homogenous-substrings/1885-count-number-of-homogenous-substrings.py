class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        l, r = 0, 0        
        while r <= len(s):
           
            if r == len(s) or not s[r] == s[l]:
                total += ((1 + r - l) * (r - l) // 2)
                l = r                       
            r += 1
        
        return total % (10 ** 9 + 7)


            