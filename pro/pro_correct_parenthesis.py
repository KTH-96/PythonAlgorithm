def solution(s):
    count: int = 0
    if len(s) < 2:
        return False

    for p in s:
        if count == 0 and p == ')':
            return False
        else:
            if p == '(':
                count += 1
            else:
                count -= 1

    return count == 0
