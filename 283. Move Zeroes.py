class Solution:
    def moveZeroes(self, nums) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1



tt = Solution()
print(tt.moveZeroes([0,1,0,3,12]))