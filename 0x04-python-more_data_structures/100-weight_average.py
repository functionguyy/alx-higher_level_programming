#!/usr/bin/python3

def weight_average(my_list: list = []):
    """Function that returns the weighted average of all integers tuple
    `(<score>, <weight>)`

    Args:
        my_list: empty list object or list of tuple or empty
    Return:
        weight average of all integers or zero
    """

    def weightAvg():
        return lambda x, y: x/y

    if type(my_list) is list:
        if len(my_list) == 0:
            return 0
        sumOfScoreWeightProduct = 0
        sumOfWeight = 0
        weightAverage = weightAvg()
        for s, w in my_list:
            scoreWeightProduct = s * w
            sumOfScoreWeightProduct += scoreWeightProduct
            sumOfWeight += w
        return weightAverage(sumOfScoreWeightProduct, sumOfWeight)
    else:
        return 0
