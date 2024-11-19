import numpy as np

table = np.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, encoding='utf-8', skip_header=True)

maxkk = np.nanmax([row[3] for row in table])
kkil = np.where([row[3] == maxkk for row in table])[0]
kkl = {}
for n in kkil:
    kkl[n] = table[n][1] 
print(kkl[max(kkl)])

mins = np.nanmin([row[9] for row in table]) 
sil = np.where([row[9] == mins for row in table])[0]
sl = {}
for n in sil:
    sl[n] = table[n][1]
print(sl[min(sl)])

maxp = np.nanmax([row[4] for row in table]) 
pil = np.where([row[4] == maxp for row in table])[0]
pl = [table[n][1] for n in pil]
print(min(pl))

maxc = np.nanmax([row[20] for row in table]) 
cil = np.where([row[20] == maxc for row in table])[0]
cl = [table[n][1] for n in cil]
print(*cl)