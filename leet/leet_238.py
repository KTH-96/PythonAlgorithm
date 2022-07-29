from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        p = 1

        for num in nums:
            result.append(num)
            p *= num

        p = 1
        for i in range(len(result) - 1, -1, -1):
            p *= result[i]
            result[-i] = p

        return result
