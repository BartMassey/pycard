from pycard import *
from math import comb

# Probability of flopping a set. A "set" here includes quads: it
# would not be too hard to change this, but I think folks hoping
# for a set will be perfectly happy with quads.

# https://upswingpoker.com/odds-flopping-each-poker-hand/
p_known = 0.118

# Calculated probability

# This is the number of possible draws
# once you are holding a given pocket pair.
ndraws = comb(50, 3)

# This is the number of ways you can miss your set
# by hitting three other cards.
nmisses = comb(48, 3)

# The probability is 1 - unfavorable outcomes / total outcomes
p_calced = 1.0 - nmisses / ndraws

# Sampled probability. Without loss of generality,
# we will hold pocket aces.
p_sampled = sample(
    1_000_000,
    3,
    lambda draw: any(rank(c) == 1 for c in draw),
    deck=fresh_deck()[2:],
)

# "Exact sampled" probability. This is computed over all
# possible draws.
found, total = sample_all(
    3,
    lambda draw: any(rank(c) == 1 for c in draw),
    deck=fresh_deck()[2:],
)
p_counted = found / total

# These should agree to at least 2 decimal places.
print(p_known, p_calced, p_sampled, p_counted)
