class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # 1+3+5+... = k^2
        # 2+4+6+... = k(k+1)
        
        low = 1
        high = red + blue

        while low <= high:
            mid = (low + high) // 2
            evenRow = mid//2
            oddRow = (mid+1)//2

            if red >= oddRow**2 and blue >= evenRow*(evenRow+1):
                low = mid + 1
                # print(f"case#1: {low}, {high}")
            elif blue >= oddRow**2 and red >= evenRow*(evenRow+1):
                low = mid + 1
                # print(f"case#2: {low}, {high}")
            else:
                high = mid - 1
                # print(f"case#3: {low}, {high}")

        return high