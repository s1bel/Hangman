import math


def logistic(x):
    exp_x = math.exp(x)
    return exp_x / (exp_x + 1)


print(round(logistic(int(input())), 2))
