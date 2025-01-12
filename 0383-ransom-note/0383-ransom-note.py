class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCount = Counter(magazine)
        noteCount = Counter(ransomNote)
        
        for char, count in noteCount.items():
            if magazineCount[char] < count:
                return False

        return True