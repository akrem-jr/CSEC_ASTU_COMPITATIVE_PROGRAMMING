class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_limit = int(c**0.5) + 1
        
        for i in range(max_limit):
            # Calculate j using a^2 + b^2 = c
            j = c - i*i
            
            # Check if j is a perfect square
            if (j >= 0) and (int(j**0.5)**2 == j):
                return True
        
        return False
