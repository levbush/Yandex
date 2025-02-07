def space_game(text: str) -> None:
    print('Вы проиграли' if text.count(' ') % 2 else 'Вы выиграли')