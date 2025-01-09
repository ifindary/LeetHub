class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n+1):
            a = i%3 == 0
            b = i%5 == 0
            tempStr = ""

            if a:
                tempStr += "Fizz"
            if b:
                tempStr += "Buzz"
            if tempStr == "":
                tempStr = str(i)
            
            ans.append(tempStr)
        
        return ans