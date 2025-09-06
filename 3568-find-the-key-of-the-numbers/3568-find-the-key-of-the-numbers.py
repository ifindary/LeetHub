class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        deque1 = deque(str(num1))
        deque2 = deque(str(num2))
        deque3 = deque(str(num3))

        while len(deque1) < 4:
            deque1.appendleft('0')

        while len(deque2) < 4:
            deque2.appendleft('0')

        while len(deque3) < 4:
            deque3.appendleft('0')

        ans = 0

        for i in range(4):
            ans += min(int(deque1[i]), int(deque2[i]), int(deque3[i])) * 10**(3-i)

        return ans