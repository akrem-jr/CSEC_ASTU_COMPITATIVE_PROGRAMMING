class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        a = [skill[i]+skill[n-i-1] for i in range(n//2)]
        if len(set(a)) != 1: return -1
        return sum(skill[i]*skill[n-i-1] for i in range(n//2)) 
        
