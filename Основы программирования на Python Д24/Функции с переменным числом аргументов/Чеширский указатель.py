s = input().split()
first, last = s[0].lower(), s[-1].lower()
print(*[word for word in s[1:-1] if first <= word.lower() <= last])