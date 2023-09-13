class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      i = 0          #pointer for s
      j = 0          #pointer for t

      while i < len(s) and j < len(t) :
        if s[i] == t[j] :    #check the conditionn is true or not
          i = i + 1

        j = j + 1

      return True if i == len(s) else False        