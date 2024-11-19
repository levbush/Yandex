n1, n2, n3 = int(input()), int(input()), int(input())
st = [input() for _ in range(n1 + n2 + n3)]
s = [i for i in st if st.count(i) == 2]
print(int(len(s) / 2) if int(len(s) / 2) else 'NO')
