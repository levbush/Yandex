n1, n2 = int(input()), int(input())
st = set()
c = 0
for _ in range(n1 + n2):
    s = input()
    if s in st:
        c += 1
    st.add(s)
c *= 2
print((n1 + n2 - c) if (n1 + n2 - c) else 'NO')
