s = input('enter a sentance: ')
def is_palindrome(s: str) -> bool :
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome(s))
