class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] *26
        base = ord('a')
        for ch in s:
            freq[ord(ch) - base] += 1
        for ch in t:
            freq[ord(ch) - base] -= 1
            if freq[ord(ch) - base] < 0:
                return False
        return True


          