class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 1

        for b in range(1 , len(nums)) :
            if nums[b] != nums[b - 1] :
                nums[a] = nums[b]
                a = a + 1

        return a