data = """A,a  .- ⓘ
B,b  -... ⓘ
C,c  -.-. ⓘ
D,d  -.. ⓘ
E,e  . ⓘ
F,f  ..-. ⓘ
G,g  --. ⓘ
H,h  .... ⓘ
I,i  .. ⓘ
J,j  .--- ⓘ
K,k  -.- ⓘ
L,l  .-.. ⓘ
M,m  -- ⓘ
N,n  -. ⓘ
O,o  --- ⓘ
P,p  .--. ⓘ
Q,q  --.- ⓘ
R,r  .-. ⓘ
S,s  ... ⓘ
T,t  - ⓘ
U,u  ..- ⓘ
V,v  ...- ⓘ
W,w  .-- ⓘ
X,x  -..- ⓘ
Y,y  -.-- ⓘ
Z,z  --.. ⓘ"""

data_dict = {' ': ' '}
for row in data.split('\n'):
    data_dict[row.split()[0][-1]] = row.split()[1]
for word in input().lower().split():
    word_answer = ''
    for letter in word:
        word_answer += data_dict[letter] + ' '
    print(word_answer.strip())