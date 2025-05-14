class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = []

        for operation in operations:
            if operation == "+":
                ops.append(ops[-1]+ops[-2])
            elif operation == "D":
                ops.append(ops[-1]*2)
            elif operation == "C":
                ops.pop()
            else:
                ops.append(int(operation))
            
        return sum(ops)
            