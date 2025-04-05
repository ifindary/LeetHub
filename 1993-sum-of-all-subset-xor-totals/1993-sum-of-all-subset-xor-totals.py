class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = sum(nums)

        for i in range(2, len(nums)+1):
            subsets = combinations(nums, i)

            for subset in subsets:
                tmp = subset[0]

                for j in range(1, len(subset)):
                    tmp = tmp ^ subset[j]

                ans += tmp

        return ans