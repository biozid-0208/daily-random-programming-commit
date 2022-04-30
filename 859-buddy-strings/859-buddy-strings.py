class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count = 0 
        miss_s = []
        miss_goal = []
        if len(s) != len(goal) or len(s) == 1:
            return False
        if len(s)==2:
            return s[::-1] == goal
        
        if s == goal:
            return len(set(s)) < len(s)
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                miss_s.append(s[i])
                miss_goal.append(goal[i])
        return count == 2 and set(miss_s) == set(miss_goal)