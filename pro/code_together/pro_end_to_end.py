def solution(n, words):
    words_dict = {words[0]}

    end: str = words[0][-1]
    for i in range(1, len(words)):
        if words[i][0] != end or words[i] in words_dict:
            return [i % n + 1, i // n + 1]
        words_dict.add(words[i])
        end = words[i][-1]
    return [0, 0]
