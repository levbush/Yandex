def lucky(ticket):
    ticket = list(map(int, list(str(ticket)[::-1])))
    last = list(map(int, list(str(lastTicket)[::-1])))  # type: ignore
    return 'Счастливый' if sum(ticket[:3]) == sum(ticket[3:]) and sum(last[:3]) == sum(last[3:]) else 'Несчастливый'