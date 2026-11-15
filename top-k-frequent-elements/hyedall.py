"""
https://leetcode.com/problems/top-k-frequent-elements/description/

시간 복잡도: O(n)
공간 복잡도: O(n)
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, cnt in counts.items():
            buckets[cnt].append(num)
            
        sorted_nums = [item for bucket in buckets for item in bucket]
        return sorted_nums[-k:]
