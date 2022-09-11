import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(map(list, itertools.permutations(nums)))
        results = []
        prev_elements = []

        def dfs(elements):
            print("start dfs, elements len", len(elements))
            if len(elements) == 0:
                results.append(elements[:])

            for e in elements:
                next_elements = elements[:]
                print("next elements", next_elements)
                next_elements.remove(e)
                print("next elements after remove", next_elements)

                prev_elements.append(e)
                print("prev_elements after append", prev_elements)
                dfs(next_elements)
                prev_elements.pop()
                print("prev_elements after pop", prev_elements)

        dfs(nums)
        return results

