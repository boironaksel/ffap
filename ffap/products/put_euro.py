import numpy as np
from scipy.stats import norm

"""
Black Scholes Merton BSM model
spot = Stock price
strike = Strike price
N() = standard normal cumulative distribution function 
Put_price = K*N(-d2)-S*N(-d1)
d1 = [ln(spot/strike) + (rate + vol²/2)*(T-t)] / [vol * sqrt(T-t)]
d2 = d1 - [vol * sqrt(T-t)]
"""


def pull_euro_bsm(spot=90, strike=100, time_to_maturity=1, rate=0.1, vol=0.2):
    d1 = (np.log(spot / strike) + (rate + vol ** 2 / 2) * time_to_maturity) / (vol * np.sqrt(time_to_maturity))
    d2 = d1 - (vol * np.sqrt(time_to_maturity))
    return strike * norm.cdf(-d2) - spot * norm.cdf(-d1)


print(pull_euro_bsm())

# end
