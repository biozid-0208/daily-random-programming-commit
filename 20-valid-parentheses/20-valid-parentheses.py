class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        stk = []
        for e in s:
            if e in opening:
                stk.append(e)
            else:
                indx = closing.index(e)
                if stk == []:
                    return False
                if stk != []  and indx != opening.index(stk.pop()):
                    return False
                    
        return True if stk == [] else False
                    
            
        