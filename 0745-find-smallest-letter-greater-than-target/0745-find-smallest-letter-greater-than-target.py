class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()

        for letter in letters:
            if letter > target:
                return letter

        return letters[0]