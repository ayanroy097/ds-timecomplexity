arrSample = list(map(int, input().split()))
duplicates = []
firstSum = arrSample[0]+arrSample[1]
firstIndex = 0
secondIndex = 1
for i in range(len(arrSample)-1):
    j = i+1
    for k in range(j, len(arrSample)):
        sIter = arrSample[i]+ arrSample[j]
        if abs(firstSum) > abs(sIter):
            firstIndex = i
            secondIndex = k
            firstSum = sIter
print("Pair with minimum sum is :")
print(f'{arrSample[firstIndex]}+{arrSample[secondIndex]} = {firstSum}')

print("Time Complexity = O(n^2)")
