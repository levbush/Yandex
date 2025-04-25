def x(x):
    return x


def sqrt_fun(x):
    return x ** 0.5


for _ in range(int(input())):
    cmd = input().split()
    match cmd[0]:
        case 'define':
            globals()[cmd[1]] = 'lambda el: '
            for i in range(2, len(cmd)):
                globals()[cmd[1]] += cmd[i] + ('(el)' if cmd[i] in globals() and cmd[i] != cmd[1] else '') + ' '
            globals()[cmd[1]] = eval(globals()[cmd[1]])
        case 'calculate':
            for el in map(int, cmd[2:]):
                print(globals()[cmd[1]](el), end=' ')
            print()