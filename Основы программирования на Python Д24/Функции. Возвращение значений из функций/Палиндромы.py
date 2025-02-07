def palindrome(s: str) -> str:
    return 'Палиндром' if s.lower().replace(' ', '') == s[::-1].lower().replace(' ', '') else 'Не палиндром'