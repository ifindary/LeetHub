class Solution(object):
    def satisfiesConditions(self, grid):
        # reference : https://leetcode.com/problems/check-if-grid-satisfies-conditions/solutions/5162662/python-3-5-lines-sets-t-s-96-67

        # pairwise(): 연속된 두 개 요소씩 묶어줌 (python 3.10 이상)
        # ex. [1,2,3,4] -> (1,2), (2,3), (3,4)
        # grid[0]만 확인하면 됨(열마다 값이 모두 같아야 하고, 열마다 값이 다르다면 다음 for문에서 검출됨)
        for left, right in pairwise(grid[0]):
            if left == right: return False

        # *grid: 2차원 배열을 행 기준으로 풀어서 전달
        # zip(*grid): 행을 열로 묶음(transpose 효과)
        # 즉 어떤 열의 집합 크기가 1인지 검사
        for setNum in list(map(set, zip(*grid))):
            if len(setNum) != 1: return False

        return True