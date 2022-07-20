import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = re.sub('[^a-z0-9]', '',s)
        # 슬라이싱 역순으로 뒤집기
        return s == s[::-1]
