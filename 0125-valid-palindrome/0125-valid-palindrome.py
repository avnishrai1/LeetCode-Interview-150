class Solution:
    def isPalindrome(self, s: str) -> bool:
        #firstly conert all the uppercase into lowercase
        isLower = s.lower()
        #print(isLower)

        #secondly remove all thee  alphanumeric char from the string 
        newS = ""
        for ch in isLower :
          if ch.isalnum() :
            newS = newS + ch

        print(newS)

        #finally check it reads the same forward and backward
        firstSTR = 0
        lastSTR = len(newS) - 1
        while firstSTR < lastSTR :
          if newS[firstSTR] !=  newS[lastSTR] :
            return False 

          firstSTR = firstSTR + 1
          lastSTR = lastSTR - 1

        return True