horses = [True] * 10


def do_bet(horse, amount):
    if not amount or not (0 < horse <= 10) or not horses[horse - 1]:
        print('Что-то пошло не так, попробуйте еще раз')
        return
    print(f'Ваша ставка в размере {amount} на лошадь {horse} принята')
    horses[horse - 1] = False