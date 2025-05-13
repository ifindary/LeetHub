class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = []

        for operation in operations:
            if operation == "+":
                ops.append(str(int(ops[-1])+int(ops[-2])))
            elif operation == "D":
                ops.append(str(int(ops[-1])*2))
            elif operation == "C":
                ops.pop()
            else:
                ops.append(operation)
            
        ans = 0

        for n in ops:
            ans += int(n)

        return ans
            