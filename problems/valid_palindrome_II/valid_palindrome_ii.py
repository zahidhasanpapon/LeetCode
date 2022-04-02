def validPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    def check_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1

        return True

    while left < right:
        if s[left] != s[right]:
            return check_palindrome(s, left, right - 1) or check_palindrome(s, left + 1, right)

        left, right = left + 1, right - 1

    return True

result = validPalindrome("aba")
print(result)
