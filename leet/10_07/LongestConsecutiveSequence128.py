from typing import List


class LongestConsecutiveSequence128:

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_dict = {}
        for num in nums:
            num_dict[num] = True

        longest_stack = 1
        for num in num_dict:
            if num - 1 not in num_dict:
                stack = 1
                next_target = num + 1
                while next_target in num_dict:
                    stack += 1
                    next_target += 1
                    longest_stack = max(longest_stack, stack)

        return longest_stack
