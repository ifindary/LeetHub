class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        
        for i in range(2**n):
            binary = format(i, f'0{n}b')

            if str(binary) not in nums:
                return binary