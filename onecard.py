# Probability of getting some specific card in a 2-card
# starting hand.

from math import comb

from pycard import *

p_calced = 51 / comb(52, 2)

# Without loss of generality, look for the Ace of Clubs.

p_sampled = sample(
    1_000_000,
    2,
    lambda draw: 1 in draw,
    deck=fresh_deck(),
)

found, total = sample_all(
    2,
    lambda draw: 1 in draw,
    deck=fresh_deck(),
)
p_counted = found / total

# These should agree to at least 2 decimal places.
print(p_calced, p_sampled, p_counted)
