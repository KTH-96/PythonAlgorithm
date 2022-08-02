def solution(n, times):
    result = 0
    times.sort()
    # 최소 시간과 최대 시간
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        checked_people = 0 # 입국 심사가 완료된 사람 수
        for time in times:
            checked_people += mid // time # 시간안에 입국 심사가 가능한사람 수
            if checked_people >= n: # 중간에 인원수 보다 체크인원수가 많아지면 빠져나가야 함
                break

        if checked_people >= n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result
