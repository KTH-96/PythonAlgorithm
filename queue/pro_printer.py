from collections import deque

def solution(priorities, location):
    # enumerate로 (인덱스, 실제값)으로 만들기
    queue = deque(enumerate(priorities))
    answer: int = 0

    while True:
        cur = queue.popleft()
        # 우선순위가 데큐안에 하나라도 큰게 남아있다면 뒤로 보내고 아니라면 지우고 +1
        if any([cur[1] < ip[1] for ip in queue]):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                break
    return answer
