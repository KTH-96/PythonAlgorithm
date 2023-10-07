from typing import List


class DailyTemperatures739:
    # [73,74,75,71,69,72,76,73] temperatures
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day, _ = stack.pop()
                answer[prev_day] = day - prev_day

            stack.append((day, temp))

        return answer
