class Solution:
    def isPalindrome(self, s: str) -> bool:
      #firstly lowercase the letter 
      sLower = s.lower()

      #secondly remove all the alphanumeric ch and spaces from the string
      sAlphaNum = ""
      for ch in sLower :
        if ch.isalnum() :
          sAlphaNum = ch + sAlphaNum

      print(sAlphaNum)

      #finally check the string froward and backward is same or not 
      strpointer = 0
      endpointer = len(sAlphaNum) - 1

      while strpointer < endpointer :
        if sAlphaNum[strpointer] != sAlphaNum[endpointer] :
          return False

        strpointer = strpointer + 1
        endpointer = endpointer - 1

      return True
        