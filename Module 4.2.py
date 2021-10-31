
def isPalindrome(word):
    length = len(word)
    inv_word = word[::-1]
    if word == inv_word:
        answer = True
    else:   
        answer = False
    print(answer)
  

isPalindrome("kajak")