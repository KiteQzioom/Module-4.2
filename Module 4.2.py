
def isPalindrome(word):
    length = len(word)
    inv_word = word[::-1]
    if word == inv_word:
        answer = True
    else:   
        answer = False
    print(answer)
    
"""
The function isPalindrome takes an input of a string and checks if it is a palindrome. It outputs the answer in boolean as True or False.
""" 

isPalindrome("kajak")
isPalindrome("stół")