def solution(dirs):
    command = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    # set자료구조로 중복제거
    visit = set()
    x = 0
    y = 0
    for move in dirs:
        nx = x + command[move][0]
        ny = y + command[move][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if nx < x or ny < y:
                visit.add(((nx, ny), (x, y)))
            else:
                visit.add(((x, y), (nx, ny)))
            x = nx
            y = ny

    return len(visit)
