class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1     

        while l < r :
          final = numbers[l] + numbers[r]

          if final < target :
            l += 1

          elif final > target :
            r -= 1
            
          else :
            return [l+1, r+1]

        return []       # time cmpllexity O(n)