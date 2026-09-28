class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        for char in s: # Loop for all chars in s
            if(char in count): # if its in count already we add a variable to it
                count[char] = count[char] + 1
            else: # otherwise we add the char
                count[char] = 1

        for char in t:
            if char not in count:
                return False
            
            count[char] -= 1

            if count[char] < 0:
                return False


        return True

        
        