class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1

        while l < r :
            result = numbers[l] + numbers[r]

            if result < target :
                l = l + 1

            elif result > target :
                r = r - 1

            else :
                return [l+1, r+1]

        return []