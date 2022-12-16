from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(num, index, element):
            if num < 0:
                return
            if num == 0:
                result.append(element)
                return

            for i in range(index, len(candidates)):
                dfs(num - candidates[i], i, element + [candidates[i]])


        dfs(target, 0 , [])

        return result
