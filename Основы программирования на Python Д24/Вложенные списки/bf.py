li = [0] * 30000
now = 0
jumps = {}
text = input()
stack = []
for i, act in enumerate(text):
    if act == '[':
        stack.append(i)
    elif act == ']':
        j = stack.pop()
        jumps[i], jumps[j] = j, i

i = 0
while i < len(text):
    act = text[i]
    if act == '+':
        li[now] = (li[now] + 1) % 256
    elif act == '-':
        li[now] = (li[now] - 1) % 256
    elif act == '>':
        now = now + 1
    elif act == '<':
        now = now - 1
    elif act == '.':
        print(li[now])
    elif act == '[':
        if li[now] == 0:
            i = jumps[i]
    elif act == ']':
        i = jumps[i]
        continue
    i += 1