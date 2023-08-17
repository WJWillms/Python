class Solution:
    def isPalindrome(self, x: int) -> bool: 
        y=str(x)
        start = 0
        ending = len(str(x)) - 1
        while start <= ending:
            if y[start] == y[ending]:
                start += 1
                ending -= 1
            else:
                return False
        return True
		
#We can turn the number 'x' into a string using the str() function/
#From there we can interate through the string character by character.
#We have one comparator start from the first character and one from the last.
#The while loop will return false if both characters don't match.
#If we exit the while loop that means no faults were detected and the number is a palindrome.
#len() function is used to determine the last number in the string and we use -1 since we start from 0 not 1.