class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
     num2=[]
     for i in nums :
         num2.append(int(i*i))
     num3=sorted(num2) 
     return num3  
