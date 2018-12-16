# FFAP
##Fucking Financial Analysis Package
*by Aksel Boiron*

### Installation / Upgrade
```cmd
pip install ffap
pip install ffap==1.0
pip install --upgrade ffap
```

###Examples
* Products
    * European call
    ```python
  import ffap
  ffap.call_euro_bsm(spot=110, strike=100, time_to_maturity=1, rate=0.1, vol=0.2)
    ```