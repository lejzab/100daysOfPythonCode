import random


def get_random_number(multiplier: int = 10) -> float:
    """return random number from [0, multiplier)
    """
    return random.random() * multiplier


def main():
    print(f'ala {get_random_number():.4f}')


if __name__ == '__main__':
    print('no cześć')
    main()
