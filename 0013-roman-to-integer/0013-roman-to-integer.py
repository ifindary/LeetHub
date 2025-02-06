class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    
        total = 0

        for i in range(len(s)-1):
            if romanValues[s[i]] < romanValues[s[i+1]]:
                total -= romanValues[s[i]]
            else:
                total += romanValues[s[i]]

        total += romanValues[s[-1]]

        return total