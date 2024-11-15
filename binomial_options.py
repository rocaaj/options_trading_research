import numpy as np 
import pandas as pd 
import argparse as ap
import math

# calculates probability of upside
def u_prob(risk_free, su, sd):
    e = math.e
    u_prob = (math.pow(e, risk_free) - sd) / (su - sd)

    return u_prob

# calculates probability of downside
def d_prob(u_prob):
    d_prob = 1 - u_prob
    
    return d_prob

# calculate upside call value
def u_call(su, stock_price):
    u_call = su * stock_price
    
    return u_call

# calculate downside call value
def d_call(sd, stock_price):
    d_call = sd * stock_price

    return d_call

# calculate call value
def call_value(u_call, u_prob, d_call, d_prob, risk_free):
    e = math.e
    call_value = (u_call * u_prob) + (d_call * d_prob) / math.pow(e, risk_free)

    return call_value


def main():
    ## Euro option price: 1y
    parser = ap.ArgumentParser(description='Binomial Options Calculator')
    parser.add_argument('strike', help='Price at which the option holder has the right to buy (call option) or sell (put option)') # price at which the option holder has the right to buy (call option) or sell (put option)
    parser.add_argument('stock_price', help='Current price of asset underlying the option') # current price of asset underlying the option
    parser.add_argument('risk_free', help='Return on an investment with no risk (discounts future payoffs back to present value)') # return on an investment with no risk (discounts future payoffs back to present value)
    parser.add_argument('su', help='upside multiple (how much stock price may go up per step)') # upside multiple (how much stock price may go up per step)
    parser.add_argument('sd', help='downside multiple (how much stock price may go down per step)') # downside multiple (how much stock price may go down per step)
    parser.add_argument('--time_step', default=1, help='Time step given in year(s)')

    args = parser.parse_args()

if __name__ == '__main__':
    main()