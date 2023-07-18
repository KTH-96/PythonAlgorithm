from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 배열의 길이 1만 n^2 까지
        # 배열 안에 숫자 및 타겟 크기 -10억 ~ 10억 -> 2개를 더하니 int가능
        # null일 가능성과 정답이 없을 가능성 없음
        if len(nums) == 2:
            return [0, 1]

        # nlogn
        sorted_nums = sorted(nums)
        print(sorted_nums)
        left_pointer, right_pointer = 0, len(sorted_nums) - 1
        # n
        while left_pointer < right_pointer:
            sum_number = sorted_nums[left_pointer] + sorted_nums[left_pointer]
            if target == sum_number:
                return [left_pointer, right_pointer]
            elif target < sum_number:
                right_pointer -= 1
            elif target > sum_number:
                left_pointer += 1

        return [0, 1]

    def two_sum_hash_table(self, nums: List[int], target: int) -> List[int]:
        # 현재 값에서 타겟 값을 뺀값이 정답이 되는 값인데 num_dict에 저장한 값, 인덱스를 사용해 인덱스 값을 가져온다.
        num_dict: Dict[int, int] = {}

        for i, number in enumerate(nums):
            target_number = target - number
            if target_number in num_dict:
                return sorted([num_dict[target_number], i])

            num_dict[number] = i

        return []


solution_instance = Solution()
print(solution_instance.twoSum([3, 2, 4], 6))
