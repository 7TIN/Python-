# https://www.hackerrank.com/contests/mountblue-technologies/challenges/breaking-best-and-worst-records
def breakingRecords(scores):
    
    low = []
    high = []
    maxx = scores[0]
    minn = scores[0]
    for i in scores:
        if i > maxx:
            maxx = i
            high.append(i)
        if i < minn:
            minn = i
            low.append(i)
    return len(high),len(low)