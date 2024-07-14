#https://www.hackerrank.com/contests/mountblue-technologies/challenges/quicksort1/submissions/code/1380114078
def quickSort(arr):
    # Write your code here
    equals = []
    left = []
    right = []
    pivot = arr[0]
    for i in range(len(arr)):
        if arr[i] == pivot :
            equals.append(arr[i])
        elif arr[i] < pivot :
            left.append(arr[i])
        elif arr[i] > pivot :
            right.append(arr[i])
        else:
            continue
    return left + equals + right