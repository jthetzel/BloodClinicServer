"""
Prediction functions
"""


from random import uniform
from datetime import datetime, timedelta
from bin_loader import pull_day


MAX = 100
BINS = 24
OPEN = 7
CLOSE = 15


def get_mock_prediction(date=None, clinics=['mp', 'wf', 'hs', 'sc']):
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


def get_prediction(date=None, clinics=['mp', 'wf', 'hs', 'sc']):
    if not date:
        now = datetime.now()

        # for demo, because demo is on a Sunday
        now = now + timedelta(days=1)

        current_rate = {}
        daily_rates = {}
        for clinic in clinics:
            rates = pull_day(clinic.upper(), now)
            rates = [rate if rate else 0 for rate in rates]
            daily_rates[clinic] = rates
            current_rate[clinic] = rates[now.hour]

    return current_rate, daily_rates


if __name__ == '__main__':
    print(get_prediction()[0])
    print(get_prediction()[1])
