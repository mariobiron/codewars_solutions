# Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:
#
# 1+1+1+1, 1+1+2, 2+2.
# The order of coins does not matter:
#
# 1+1+2 == 2+1+1
# Also, assume that you have an infinite amount of coins.
#
# Your function should take an amount to change and an array of unique denominations for the coins:
#
#   count_change(4, [1,2]) # => 3
#   count_change(10, [5,2,3]) # => 4
#   count_change(11, [5,7]) # => 0

def recursive_count(change, coins, nb_coins):
    if (change == 0):
        return 1
    elif (change < 0) or (nb_coins <= 0 and change >= 1):
        return 0
    else:
        return recursive_count(change, coins, nb_coins-1) + recursive_count(change-coins[nb_coins-1], coins, nb_coins)

def count_change(money, coins):
    return recursive_count(money, coins, len(coins))

print(count_change(4, [1, 2])) #, 3)
print(count_change(10, [5, 2, 3])) #, 4)
print(count_change(11, [5, 7])) #, 0)

# def recursive_count(change, coins, nb_coins):
#     if (change == 0):  # If change is 0 then there is 1 solution (do not include any coin)
#         return 1
#     elif (change < 0) or (nb_coins <= 0 and change >= 1):  # If change is less than 0 OR If there are no coins and change is greater than 0, then no solution exist
#         return 0;
#     else:
#         return recursive_count(change, coins, nb_coins-1) + recursive_count(change-coins[nb_coins-1], coins, nb_coins);
#
# def count_change(money, coins):
#     return recursive_count(money, coins, len(coins))

# def count_change(money, coins):
#     dp = [1]+[0]*money
#     for coin in coins:
#         for x in xrange(coin,money+1):
#             dp[x] += dp[x-coin]
#     return dp[money]

# def count_change(money, coins):
#
#     ways = [1] + [0] * (money + 1)
#
#     for coin in coins:
#
#         for i in range(coin, money + 1):
#
#             ways[i] += ways[i - coin]
#
#     return ways[money]

# def count_change(money, coins):
#         results = [0] * (money + 1)
#         results[0] = 1
#         for i in coins:
#                 for j in xrange(i, money + 1):
#                         results[j] += results[j - i]
#         return results[money]

# def count_change(money, coins):
#     A = [1] + [0]*money
#     for c in coins:
#         A = [sum(A[:k+1][::-c]) for k in range(money+1)]
#     return A[-1]

# def count_change(money, coins):
#     #
#     if money == 0: return 1
#     if money < 0: return 0
#     if not coins: return 0
#     return count_change(money-coins[0], coins) + count_change(money, coins[1:])