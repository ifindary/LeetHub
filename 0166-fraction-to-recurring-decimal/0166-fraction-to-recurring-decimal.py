class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        if (numerator > 0) ^ (denominator > 0): # numerator*denominator<0
            ans = ['-']
        else:
            ans = []

        a, b = abs(numerator), abs(denominator)

        ans.append(str(a//b))

        a %= b

        if a == 0:
            return ''.join(ans)
        else:
            ans.append('.')

        d = {}

        while a:
            d[a] = len(ans)
            a *= 10
            ans.append(str(a//b))
            a %= b

            if a in d:
                ans.insert(d[a], '(')
                ans.append(')')
                break
    
        return ''.join(ans)