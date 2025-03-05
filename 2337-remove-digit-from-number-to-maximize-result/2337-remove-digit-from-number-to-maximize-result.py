class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        candidates = []

        for i in range(len(number)):
            if number[i] == digit:
                lastIndex = i

                if i < len(number)-1 and number[i] < number[i+1]:
                    return number[:i] + number[i+1:]

        return number[:lastIndex] + number[lastIndex+1:]