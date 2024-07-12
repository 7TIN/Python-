# https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    x = "NO"
    y = "YES"
    if v1 <= v2:
        return x
    if (x1-x2) % (v1-v2) == 0:
        return y
    else:
        return x