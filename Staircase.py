# https://www.hackerrank.com/contests/mountblue-technologies/challenges/staircase/problem
def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        for k in range(n-i):
            print(" ",end="")
        for j in range(i):
            print("#",end ="")
        print()


   #
  ##
 ###
####