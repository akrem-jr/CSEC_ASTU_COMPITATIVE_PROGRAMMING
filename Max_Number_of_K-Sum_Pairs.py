class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_count = {}
        total = 0

        for num in nums:
            r = k - num

            if r in num_count and num_coun[r] > 0:
                total += 1
                num_count[r] -= 1
            else:
                num_count[num] = num_count.get(num, 0) + 1

        return total
