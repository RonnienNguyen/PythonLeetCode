# Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

# What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

# Input
# The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).

import math

def min_flagstones(n, m, a):
    total_area = n * m
    flagstone_area = a * a
    num_flagstones = total_area / flagstone_area
    return math.ceil(num_flagstones)

# Example usage:
n, m, a = 6, 6, 4
result = min_flagstones(n, m, a)
print(result)  # Output: 4
