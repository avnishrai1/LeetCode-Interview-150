class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #initialise two pointer, one for  hold and another one for comparsion
        p = 1

        for q in range(1, len(nums)) :
            if nums[q] != nums[q - 1] :
                nums[p] = nums[q]
                p = p + 1

        return p