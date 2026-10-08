import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

def choice_7(num_iter:int, win, loss):

    total_wins = 0
    total_loses = 0
    count = [0]

    for itter in range(0, num_iter):
        dice_one = np.random.random_integers(1, 6)
        dice_two = np.random.random_integers(1, 6)

        dices_result = dice_one + dice_two

        if dices_result == 7:
            acc = count[-1] + win
            count.append(acc)
            total_wins += 1
        else: 
            acc = count[-1] - loss
            count.append(acc)
            total_loses += 1
    
    figure = plt.figure(figsize=(14, 8))

    plt.plot(range(len(count)), count, linestyle='-', color='green', label='Choise is 7')
    plt.legend()
    plt.xlabel('Number of itterations')
    plt.ylabel('Account value')

    plt.show()

    print('\nStatistic of choice 7:\n')
    print('Total wins: ', total_wins)
    print('Total loses: ', total_loses)
    print('End value: ', count[-1])


def choice_bounders(num_iter:int, win, loss):

    total_wins = 0
    total_loses = 0
    count = [0]

    for itter in range(0, num_iter):
        dice_one = np.random.random_integers(1, 6)
        dice_two = np.random.random_integers(1, 6)

        dices_result = dice_one + dice_two

        if dices_result == 12:
            acc = count[-1] + win
            count.append(acc)
            total_wins += 1
        else: 
            acc = count[-1] - loss
            count.append(acc)
            total_loses += 1
    
    figure = plt.figure(figsize=(14, 8))

    plt.plot(range(len(count)), count, linestyle='-', color='orange', label='Choise is near bounds')
    plt.legend()
    plt.xlabel('Number of itterations')
    plt.ylabel('Account value')

    plt.show()

    print('\nStatistic of choice 7:\n')
    print('Total wins: ', total_wins)
    print('Total loses: ', total_loses)
    print('End value: ', count[-1])


def choice_random(num_iter:int, win, loss):

    total_wins = 0
    total_loses = 0
    count = [0]

    for itter in range(0, num_iter):
        dice_one = np.random.random_integers(1, 6)
        dice_two = np.random.random_integers(1, 6)

        dices_result = dice_one + dice_two

        choice = np.random.random_integers(2, 12)

        if dices_result == choice:
            acc = count[-1] + win
            count.append(acc)
            total_wins += 1
        else: 
            acc = count[-1] - loss
            count.append(acc)
            total_loses += 1
    
    figure = plt.figure(figsize=(14, 8))

    plt.plot(range(len(count)), count, linestyle='--', color='red', label='Random choice')
    plt.legend()
    plt.xlabel('Number of itterations')
    plt.ylabel('Account value')

    plt.show()

    print('\nStatistic of random choice:\n')
    print('Total wins: ', total_wins)
    print('Total loses: ', total_loses)
    print('End value: ', count[-1])


# ratio 10:1
step_win = 22
step_loss = 2

# choice_7(1000, step_win, step_loss)
# choice_bounders(1000, step_win, step_loss)
choice_random(1000, step_win, step_loss)

