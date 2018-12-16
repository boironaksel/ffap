import numpy as np
from scipy.stats import norm

"""
Black Scholes Merton BSM model
spot = Stock price
strike = Strike price
N() = standard normal cumulative distribution function 
Call_price = S*N(d1)-K*N(d2)
Put_price = K*N(-d2)-S*N(-d1)
d1 = [ln(spot/strike) + (rate + vol²/2)*(T-t)] / [vol * sqrt(T-t)]
d2 = d1 - [vol * sqrt(T-t)]
"""


def bsm(spot: float, strike: float, time_to_maturity: float, rate: float, vol: float, option: str):
    d1 = (np.log(spot / strike) + (rate + vol ** 2 / 2) * time_to_maturity) / (vol * np.sqrt(time_to_maturity))
    d2 = d1 - (vol * np.sqrt(time_to_maturity))
    if option == 'call':
        return spot * norm.cdf(d1) - strike * norm.cdf(d2)
    elif option == 'put':
        return strike * norm.cdf(-d2) - spot * norm.cdf(-d1)
    else:
        raise NameError('Option argument not \'call\' or \'put\'')
