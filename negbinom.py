# Negative Binomial Distribution demo
# Bart Massey 2025-08
# https://www.datacamp.com/tutorial/negative-binomial-distribution
# https://en.wikipedia.org/wiki/Negative_binomial_distribution

from argparse import ArgumentParser
from math import comb
from random import random

ap = ArgumentParser()
ap.add_argument("p", type=float)
ap.add_argument("k", type=int)
ap.add_argument("r", type=int)
args = ap.parse_args()

p = args.p
k = args.k
r = args.r

def pmf(p, k, r):
    return comb(k + r - 1, k) * p**r * (1 - p)**k

def cpmf(p, k, r):
    return sum(pmf(p, i, r) for i in range(k + 1))

def mean_cpmf(p, r):
    return r * (1 - p) / p

def var_cpmf(p, r):
    return r * (1 - p) / p**2

def try_pmf(p, k, r):
    nfailures = 0
    nsuccesses = 0
    while nsuccesses < r:
        if random() > p:
            nfailures += 1
        else:
            nsuccesses += 1
    return nfailures == k

def experiment_pmf(p, k, r):
    nok = 0
    for _ in range(100000):
        if try_pmf(p, k, r):
            nok += 1
    return nok / 100000

# works for p=0.6 k=5 r=5
print("pmf_calc", pmf(p, k, r))
print("pmf_exp", experiment_pmf(p, k, r))
