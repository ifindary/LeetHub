class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0

        for word in words:
            length = len(word)

            if s[0:length] == word:
                cnt += 1

        return cnt
            