class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #firstly initilaise two pointer l and m 
        l = 1
        
        #now iterate  the pointer through the loop 
        for m in range(1, len(nums)) :
            if nums[m] != nums[m - 1] :
                nums[l] = nums[m]
                l = l + 1

        return l