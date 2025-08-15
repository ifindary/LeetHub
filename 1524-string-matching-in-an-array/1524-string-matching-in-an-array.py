class Solution(object):
    def stringMatching(self, words):
        ans = []

        words.sort(key=len)

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break

        return ans