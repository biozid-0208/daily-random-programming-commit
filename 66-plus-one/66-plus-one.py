class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        end = len(d) -1
        s = d[end] + 1
        c = s // 10
        d[end] = s % 10
        end -= 1
        while c != 0 and end >= 0:
            s = d[end] + c
            c = s // 10
            d[end] = s % 10
            end -= 1
        if c != 0:
            d.insert(0, 1)
        return d
            
        
        