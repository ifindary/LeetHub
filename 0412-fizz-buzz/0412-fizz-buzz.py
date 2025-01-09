class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n+1):
            a = i%3
            b = i%5

            if a + b == 0:
                ans.append("FizzBuzz")
            elif a == 0:
                ans.append("Fizz")
            elif b == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        
        return ans