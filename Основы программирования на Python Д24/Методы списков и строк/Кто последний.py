from collections import deque
queue = deque()
for i in [input() for _ in range(int(input()))]:
    if 'Кто' in i:
        queue.append(i[19:-1])
    elif 'только ' in i:
        queue.insert(0, i[23:-1])
    else:
        try:
            print(f'Заходит {queue.popleft()}!')
        except IndexError:
            print('В очереди никого нет.')