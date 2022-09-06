import collections
import operator
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        d = sorted(collections.Counter(nums).items(), key=lambda x: x[1])

        for i in range(1, k + 1):
            (k, y) = d[-i]
            result.append(k)

        return result
