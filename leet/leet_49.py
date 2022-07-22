import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an = collections.defaultdict(list)

        for word in strs:
            an[''.join(sorted(word))].append(word)

        return list(an.values())
