# Probability of getting two cards, each of some specific
# distinct rank, in a two-card starting hand.

from math import comb

from pycard import *

p_calced = 16 / comb(52, 2)

# Without loss of generality, look for Ace-Deuce.

p_sampled = sample(
    1_000_000,
    2,
    lambda draw: sorted([rank(c) for c in draw]) == [1, 2],
    deck=fresh_deck(),
)

found, total = sample_all(
    2,
    lambda draw: sorted([rank(c) for c in draw]) == [1, 2],
    deck=fresh_deck(),
)
p_counted = found / total

# These should agree to at least 2 decimal places.
print(p_calced, p_sampled, p_counted)
