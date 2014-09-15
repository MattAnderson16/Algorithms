def Palindrome(word,first,last):
    if word[first] == word[last]:
        result = True
    elif word[first] != word[last]:
        result = False
    else:
        result = Palindrome(word,first + 1, last - 1)  
    return result

word = input("Please enter a word >> ")
first = 0
last = len(word) - 1
result = Palindrome(word,first,last)
if result:
    print("Your word is a palindrome!")
else:
    print("Your word is not a palindrome!")
