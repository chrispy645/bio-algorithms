import sys

money = int( sys.stdin.readline().rstrip() )

coins = [int(x) for x in sys.stdin.readline().rstrip().split(',')]

"""
The recurrence relation:
minNumCoins[money] = min( minNumCoins[money-coin[i]] + 1
                          ...
                          ...
                          minNumCoins[money-coin[d]] + 1 )
minNumCoins[0] = 0
"""

minNumCoins = [float('inf') for x in range(0, money+1)]
minNumCoins[0] = 0
for m in range(1, money+1):
    for i in range(0, len(coins)):
        if m >= coins[i]:
            if minNumCoins[ m-coins[i] ] + 1 < minNumCoins[m]:
                minNumCoins[m] = minNumCoins[ m-coins[i] ] + 1
print minNumCoins[money]
