"""
https://leetcode.com/problems/two-sum/

시간 복잡도: O(n)
공간 복잡도: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}

        for i, value in enumerate(nums):
            complement = target - value

            if complement in indices:
                return [indices[complement], i]

            indices[value] = i
