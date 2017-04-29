"""
Prediction functions
"""


from random import uniform


MAX = 100
BINS = 24
OPEN = 7
CLOSE = 15


def get_prediction(date=None, clinics=['one', 'two', 'three', 'four']):
    result = {}
    for clinic in clinics:
        rates = [0] * BINS
        rates[OPEN:CLOSE] = [
          uniform(0, MAX) for x in range(CLOSE - OPEN)]
        result[clinic] = rates

    return result
