class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        editedShifts = shifts.copy()
        newS = []

        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]

        for i in range(len(shifts)):
            tmp = (ord(s[i]) - ord('a') + shifts[i])%26
            newS.append(chr(tmp + ord('a')))

        return ''.join(newS)