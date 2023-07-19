# Implement pow(x, n), which calculates x raised to the power n (xn).
# Example 1:
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]

class Solution:
    def myPow(self, x, n):
        ret, pow_x = 1.0, x

        m = n if n >= 0 else -n
        while m != 0:
            if m & 1:
                ret *= pow_x
            pow_x = pow_x * pow_x
            m >>= 1

        return ret if n >= 0 else 1.0 / ret

# Example usage:
x = 2.10000
n = 3
solution = Solution()
result = solution.myPow(x, n)
print(result)
