from math import ceil


def solution(progresses, speeds):
    answer = []
    max_date = ceil((100 - progresses[0]) / speeds[0])
    count = 0

    for progresses, speeds in zip(progresses, speeds):
        date = ceil((100 - progresses) / speeds)
        print("date %d" % date)
        print("max date %d" % max_date)
        if max_date < date:
            answer.append(count)
            count = 0
            max_date = date
        count += 1

    answer.append(count)

    return answer
