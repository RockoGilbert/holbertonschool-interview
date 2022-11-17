#!/usr/bin/python3
def makeChange(coins, total):
    """
    Prototype: def makeChange(coins, total):
    Args:
      coins: list of values of coins in your possession
        (the value of a coin will always be an int > 0)
        (you can assume you have an infinite supply of each coin)
      total: amount of money you want to make change for
    Return:
      if total is <= 0: return 0
      if total cannot be met: return -1
      if total can be met: return the minimum number of coins needed
        to meet total.
    """

    
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    stack = total
    mv = 0
    cnt = 0

    while (mv < len(coins)):
        if stack == 0:
            return cnt

        if coins[mv] > stack:
            mv += 1

        else:
            stack -= coins[mv]
            cnt += 1

    return -1