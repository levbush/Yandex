def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        # sequence = sequence + [next_element]
        sequence.append(
            next_element)  # Мы не можем перезаписать глобальную переменную sequence, но можем изменить её элементы