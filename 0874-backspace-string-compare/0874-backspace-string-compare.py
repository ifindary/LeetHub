class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def edited(text: str) -> str:
            editedText = []

            for letter in text:
                if letter == "#" and editedText:
                    editedText.pop()
                elif letter != "#":
                    editedText.append(letter)

            return editedText

        return edited(s) == edited(t)