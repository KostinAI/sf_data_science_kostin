import numpy as np
from numpy import random

def random_predict(number:int=1) -> int:
    """[summary]

    Args:
        number (int, optional): [description]. Defaults to 1.

    Returns:
        int: [description]
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return(count)

#print(f'Count of tries: {random_predict(60)}')

def score_game(random_predict) -> int:
    """Avarage count of tries of guessing за 1000 подходов

    Args:
        random_predict ([type]): function of guessing

    Returns:
        int: avarage count
    """
    
    count_ls=[]
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return(score)


if __name__ == '__main__':
    #RUN
    score_game(random_predict)
    