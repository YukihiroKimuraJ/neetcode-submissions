from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for num, c in count.items():
            bucket[c].append(num)
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
