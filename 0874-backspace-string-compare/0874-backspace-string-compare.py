class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        editedS = []
        editedT = []

        for letterS in s:
            if letterS == "#" and editedS:
                editedS.pop()
            elif letterS != "#":
                editedS.append(letterS)

        for letterT in t:
            if letterT == "#" and editedT:
                editedT.pop()
            elif letterT != "#":
                editedT.append(letterT)

        if editedS == editedT:
            return True
        else:
            return False
