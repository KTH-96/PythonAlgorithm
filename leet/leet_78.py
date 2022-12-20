from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(depth, path):
            result.append(path)

            for i in range(depth, len(nums)):
                dfs(depth + 1, path + [nums[i]])

        dfs(0, [])
        return result