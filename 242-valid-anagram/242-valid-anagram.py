class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # set cannot work out, cus dupicate is not allowed 
        if len(s) != len(t):
            return False
        
        record_s, record_t = {}, {}
        for i in range(len(s)):
            record_s[s[i]] = 1 + record_s.get(s[i], 0)
            record_t[t[i]] = 1 + record_t.get(t[i], 0)
        
        for record in record_s:
            if record_s[record] != record_t.get(record, 0):
                return False
        return True