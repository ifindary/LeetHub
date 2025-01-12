class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = list(magazine)
        targets = list(ransomNote)
        
        for letter in letters:            
            if letter in targets:
                targets.remove(letter)
                if targets == []:
                    return True

        return False