from ffap.models import bsm


def call_euro_bsm(spot=90, strike=100, time_to_maturity=1, rate=0.1, vol=0.2):
    return bsm.bsm(spot, strike, time_to_maturity, rate, vol, option='call')

# end
