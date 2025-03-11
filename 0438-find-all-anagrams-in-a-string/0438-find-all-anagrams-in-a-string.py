class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cntP = Counter(p)

        for i in range(len(s)-len(p)+1):
            cntS = Counter(s[i:i+len(p)])

            if cntP == cntS:
                ans.append(i)

        return ans