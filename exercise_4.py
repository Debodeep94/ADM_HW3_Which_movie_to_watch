# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:08:16 2019

@author: leona
"""

# Returns the length of the longest  
# palindromic subsequence in seq  
def lps(seq, i, j): 
      
    # Base Case 1: If there is only 1 character  
    if (i == j): 
        return 1
  
    # Base Case 2: If there are only 2 character and both are same
    if (seq[i] == seq[j] and i + 1 == j):
        return 2
      
    # If the first and last characters match  
    if (seq[i] == seq[j]): 
        return lps(seq, i + 1, j - 1) + 2
  
    # If the first and last characters do not match 
    return max(lps(seq, i, j - 1),  
               lps(seq, i + 1, j)) 
  
# Code to run the program
if __name__ == '__main__': 
    seq = "DATAMININGSAPIENZA"
    seq = seq.lower()
    n = len(seq) 
    print("The length of the LPS is",lps(seq, 0, n - 1)) 
