#User function Template for python3
class Solution:
	def removeVowels(self, s):
		# code here
		str = ""
		
		for ch in s:
		    if ch in "aeiou":
		        continue
            str += ch
        
        return str
		