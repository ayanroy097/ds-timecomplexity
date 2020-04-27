arrSample = list(map(str, input().split()))

duplicates = []
for i in range(len(arrSample)):
    j = i+1
    for k in range(j, len(arrSample)):
        if arrSample[i] == arrSample[k]:
            if arrSample[i] not in duplicates:
                duplicates.append(arrSample[i])

print(*duplicates)

print("Time Complexity = O(n^2)")