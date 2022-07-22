import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
            # '[^\w]' w = word -> 단어를 제외한 나머지
            words = [word for word in re.sub('[^\w]', ' ', paragraph)
                     .lower().split()
                        if word not in banned]

            # counts = collections.defaultdict(int)
            # for word in words:
            #     counts[word] += 1
            #
            # return max(counts, key=counts.get)
            counts = collections.Counter(words)
            return counts.most_common(1)[0][0]
