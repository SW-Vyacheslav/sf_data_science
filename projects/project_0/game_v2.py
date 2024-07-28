"""Game: guess the number
The computer predicts and guesses the number
"""

from typing import Tuple
import numpy as np

def random_predict(number: int, min_number: int, max_number: int,
                   max_count: int = 20) -> Tuple[int, bool]:
    """Random guess

    Args:
        number (int, optional): Hidden number.
        min_number (int): minimum available hidden number
        max_number (int): maximum available hidden number
        max_count (int, optional): maximum available guesses. Defaults to 20.

    Raises:
        ValueError: if max_number < min_number

    Returns:
        Tuple[int, bool]: [Number of guesses, Is number founded in max_count steps]
    """

    if max_number < min_number:
        raise ValueError("Error: the max_number must be greater than the min_number.")

    count = 0
    is_founded = False

    while True:
        count += 1
        predict_number = np.random.randint(min_number, max_number) # random number

        if number == predict_number:
            is_founded = True
            break
        elif count == max_count:
            break

    return count, is_founded

def search_number(number: int, min_number: int, max_number: int,
                  max_count: int = 20) -> Tuple[int, bool]:
    """Number searching algorithm using range half splitting

    Args:
        number (int): Hidden number
        min_number (int): minimum available hidden number
        max_number (int): maximum available hidden number
        max_count (int, optional): maximum available guesses. Defaults to 20.

    Raises:
        ValueError: if max_number < min_number

    Returns:
        Tuple[int, bool]: [Number of guesses, Is number founded in max_count steps]
    """

    if max_number < min_number:
        raise ValueError("Error: the max_number must be greater than the min_number.")

    count = 0
    is_founded = False

    while True:
        count += 1

        # Split search range in half until find hidden number
        predicted_number = (max_number + min_number) // 2

        # Check exit condition. Choosing new range border
        if number == predicted_number:
            is_founded = True
            break
        elif count == max_count:
            break
        elif predicted_number < number:
            min_number = predicted_number
        else:
            max_number = predicted_number

    return count, is_founded

def score_game(predict_func, min_random_number: int = 1, max_random_number: int = 101) -> int:
    """For how many attempts on average for 1000 approaches our algorithm guesses

    Args:
        predict_func ([type]): prediction function
        min_random_number (int): minimum random number. Defaults to 1.
        max_random_number (int): maximum random number. Defaults to 101.

    Returns:
        int: mean number of predictions
    """
    count_ls = []
    #np.random.seed(1)

    # create array of random numbers
    random_array = np.random.randint(min_random_number, max_random_number, size=(1000))

    kwargs = { "min_number" : min_random_number,
               "max_number" : max_random_number }

    for number in random_array:
        count, is_founded = predict_func(number, **kwargs)

        if not is_founded:
            print(f"Fail! Max number of guesses reached (maximum is {count}).")
            return count

        count_ls.append(count)

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average for: {score} tries.")
    return score


if __name__ == "__main__":
    # RUN
    print("Random predict function:")
    score_game(random_predict)

    print("Search number algorithm function:")
    score_game(search_number)
