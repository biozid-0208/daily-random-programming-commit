class Solution:
    def strStr(self, h: str, n: str) -> int:
        if n == "":
            return 0
        try:
            return h.index(n)
        except: return -1
    
            
        