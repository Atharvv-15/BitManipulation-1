# Problem 2
# Single number (https://leetcode.com/problems/single-number/)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0 

        for num in nums:
            result = result ^ num

        return result

        