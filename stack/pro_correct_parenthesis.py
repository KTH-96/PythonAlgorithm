def solution(s):
    count: int = 0
    for p in s:
        if len(s) < 2 or (count == 0 and p == ')'):
            return False
        else:
            if p == '(':
                count += 1
            else:
                count -= 1

    if count == 0:
        return True
    else:
        return False
