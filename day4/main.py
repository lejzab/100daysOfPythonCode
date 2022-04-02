import random


def get_random_number(multiplier: int = 10) -> float:
    """return random number from [0, multiplier)
    """
    return random.random() * multiplier


def bor():
    _map = [['⬛️', '⬛️', '⬛️'], ['⬛️', '⬛️', '⬛️'], ['⬛️', '⬛️', '⬛️']]
    print(f'{_map[0]}\n{_map[1]}\n{_map[2]}')
    pos = input('where is do you want to put the treasure? (col, row) ')
    x, y = pos.split(' ')
    _map[int(y) - 1][int(x) - 1] = 'X'
    print(f'{_map[0]}\n{_map[1]}\n{_map[2]}')


def main():
    bor()


if __name__ == '__main__':
    main()
