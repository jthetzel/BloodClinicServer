"""
Prediction functions
"""


from random import uniform
from datetime import datetime


MAX = 100
BINS = 24
OPEN = 7
CLOSE = 15


def get_prediction(date=None, clinics=['one', 'two', 'three', 'four']):
    if not date:
        now = datetime.now()
    current_rate = {}
    daily_rates = {}
    for clinic in clinics:
        rates = [0] * BINS
        rates[OPEN:CLOSE] = [
          uniform(0, MAX) for x in range(CLOSE - OPEN)]
        daily_rates[clinic] = rates
        current_rate[clinic] = rates[now.hour]

    return current_rate, daily_rates
