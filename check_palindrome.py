
def palindrome(str):
    str = str.replace(' ','')
    print(str == str[::-1])

print('Palindrome Checker\n')
palindrome(input('Enter phrase: '))

