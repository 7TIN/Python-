# https://www.hackerrank.com/challenges/sock-merchant/problem
def sockMerchant(n, ar):
    # Write your code here
    dec = {}
    pair = 0
    for i in ar:
        if i in dec:
            dec[i]+=1
        else:
            dec[i] = 1
    # for i in dec.keys():
    #     pair+= (dec[i]//2)
    for i in dec.values():
        pair+= (i//2)
    return pair