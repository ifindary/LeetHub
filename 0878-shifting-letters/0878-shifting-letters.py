class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shiftedS = ['']*len(shifts)
        cumulativeShift = 0

        for i in range(len(shifts)-1, -1, -1):
            cumulativeShift += shifts[i]

            tmp = (ord(s[i]) - ord('a') + cumulativeShift)%26 + ord('a')
            shiftedS[i] = chr(tmp)

        return ''.join(shiftedS)