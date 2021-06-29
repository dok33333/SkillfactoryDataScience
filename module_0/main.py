import numpy as np


def game_core_v2(number):
    """
    First, we set any random number, and then we set the new value of the variables
    num_1 or num_2, depending on whether it is greater or less than the required one,
    and we get a new random number.
    The function takes a hidden number and returns the number of attempts
    """
    count, num_1, num_2 = 1, 1, 101
    predict = np.random.randint(num_1, num_2)
    while number != predict:
        count += 1
        if number > predict:
            num_1 = predict
        elif number < predict:
            num_2 = predict
        predict = np.random.randint(num_1, num_2)
    return count  # exit the loop if guessed right


def score_game(game_core):
    """
    Run the game 1000 times to find out how quickly the game guesses the number
    """
    count_ls = []
    np.random.seed(1)  # fixing RANDOM SEED so your experiment is reproducible!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v2)
