class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = sorted(list(magazine))
        targets = sorted(list(ransomNote))
        
        for letter in letters:            
            if letter in targets:
                targets.remove(letter)
                if targets == []:
                    return True

        return False