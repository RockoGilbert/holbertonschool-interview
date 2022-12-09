#!/usr/bin/python3
""" Prime Game Interview Question """


def isWinner(x, n):
    """ Assuming Maria always goes first, determine winner of each game """

    Player_1 = 0
    Player_2 = 0

    # conditional: cannot be smaller than 1 or larger than 1000
    # if x <= 0 or x > 1000:
    # return None

    if x is None or n is None or x == 0 or n == 0:
        return None

    for idx in range(x):
        P = isPrime(n[idx])
        if len(P) % 2 != 0:
            Player_1 += 1
        else:
            Player_2 += 1

    if Player_1 > Player_2:
        return "Maria"

    elif Player_2 > Player_1:
        return "Ben"
    else:
        return None


def isPrime(y):
    """ Check if list is prime """
    P = []
    tmp = [True] * (y + 1)
    for idx in range(2, y + 1):
        if tmp[idx]:
            P.append(idx)
            for k in range(idx * idx, y + 1, idx):
                tmp[k] = False
    return P

    # Maria always goes first and both play optimally.
    # There are a total of only 168 prime numbers between 1 to 1000.
    # Ben has the most wins.
    # nums is an array of consecutive integers; n.
    # x is equal to the amount of rounds of the game.
