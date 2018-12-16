import numpy as np
from scipy.stats import norm

"""
Black Scholes Merton BSM model
spot = Stock price
strike = Strike price
N() = standard normal cumulative distribution function 
Call_price = S*N(d1)-K*N(d2)
d1 = [ln(spot/strike) + (rate + vol²/2)*(T-t)] / [vol * sqrt(T-t)]
d2 = d1 - [vol * sqrt(T-t)]
"""


def call_euro_bsm(spot=110, strike=100, time_to_maturity=1, rate=0.1, vol=0.2):
    d1 = (np.log(spot / strike) + (rate + vol ** 2 / 2) * time_to_maturity) / (vol * np.sqrt(time_to_maturity))
    d2 = d1 - (vol * np.sqrt(time_to_maturity))
    return spot * norm.cdf(d1) - strike * norm.cdf(d2)


print(call_euro_bsm())

# end
