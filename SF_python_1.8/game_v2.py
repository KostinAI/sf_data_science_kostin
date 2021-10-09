"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
#from numpy import random

def random_predict(number: int = 1) -> int:
    """Угадываем число, сравнивая загаданное число с предполагаемым

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    lower_boarder = 0
    upper_boarder = 100

    while True:
        count += 1
        
        if predict_number < number:
            lower_boarder = predict_number 
        elif predict_number > number:
            upper_boarder = predict_number
        else:
            break
        
        predict_number = round((lower_boarder+upper_boarder)/2)
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
