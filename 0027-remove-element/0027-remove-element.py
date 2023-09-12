class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 

        for num1 in nums :
            if num1 != val :
                nums[i] = num1
                i = i + 1

        return i
