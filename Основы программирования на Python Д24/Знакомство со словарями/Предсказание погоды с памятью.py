weather = input()
p, q = float(input()), float(input())
days = int(input())
if weather == 'ясно':
    clear = p
    cloudy = 1 - p
else:
    clear = 1 - q
    cloudy = q
probabilities = {'ясно': [clear], 'пасмурно': [cloudy]}
for i in range(days - 1):
    element = probabilities['ясно'][0]
    new_value = []
    new_value.append(element * p)
    new_value.append(element * (1 - p))
    probabilities['ясно'] = new_value
    element = probabilities['пасмурно'][0]
    new_value = []
    new_value.append(element * q)
    new_value.append(element * (1 - q))
    probabilities['пасмурно'] = new_value
if probabilities['ясно'][0] > probabilities['пасмурно'][0]:
    print('ясно')
    print(probabilities['ясно'][0])
elif probabilities['ясно'][0] < probabilities['пасмурно'][0]:
    print('пасмурно')
    print(probabilities['пасмурно'][0])
else:
    print('равновероятно')
    print(probabilities['ясно'][0])