from typing import List


class LongestCommonPrefix:
    def longestCommonPrefix(strs: List[str]) -> str:
        prefix = []
        for chars in zip(*strs):
            #            ('f', 'f', 'f')
            if len(set(chars)) == 1:
                print(set(chars))
                prefix.append(chars[0])
            else:
                break

        return ''.join(prefix)

# print(LongestCommonPrefix.longestCommonPrefix(["flower", "flow", "flight"]))
