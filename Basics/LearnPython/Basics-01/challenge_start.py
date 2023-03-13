# Solution to programming challenge for Learning Python course
# by Luiz Araujo
#

import string

# Gets the string, keeps only alphabetic characters, lower cased.
def sanitizeString(string):
    result = ''.join(filter(str.isalpha or str.isnumeric, string))
    return result.lower()

def reversedString(string):
    result = sanitizeString(string)
    return result[::-1]

def isPalindrome(string):
    half = int((len(string) / 2))
    reverse = reversedString(string)
    if (string[0:half] == reverse[0:half]):
        return True
    return False
#     # for i in range(len(string)):
#     #     if string[i]!= string[len(string) - i - 1]:
#     #         return False
#     # return string == string[::-1]

def resultMessage(word, isPalindromeTrue):
    if word == "exit":
        print("Goodbye.")
    else:
        print(word, "is" if isPalindromeTrue == True else "is not", "a palindrome.\n")

word = " "
while word != "exit":
    # Madam, I'm Adam.
    word = input("Enter a string to test for palindrome or 'exit':")

    wordTreated = reversedString(sanitizeString(word))
    isPalind = isPalindrome(wordTreated)
    resultMessage(word, isPalind)
