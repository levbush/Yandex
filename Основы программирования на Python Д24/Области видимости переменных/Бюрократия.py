data = ()


def setup_profile(name, dates):
    global data
    data = name, dates


def print_application_for_leave():
    print(f'Заявление на отпуск в период {data[1]}. {data[0]}')


def print_holiday_money_claim(amount):
    print(f'Прошу выплатить {amount} отпускных денег. {data[0]}')


def print_attorney_letter(to_whom):
    print(f'На время отпуска в период {data[1]} моим заместителем назначается {to_whom}. {data[0]}')