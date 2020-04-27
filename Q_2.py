n = int(input())

arr1 = list(map(str, input().split()[:n]))
arr2 = list(map(str, input().split()[:n-2]))
misIndexList = []
for i in range(n-2):
    if arr1[i] != arr2[i]:
        misIndexList.append(arr1[i])
        arr2.insert(i,arr1[i])

if misIndexList == []:
    print(arr1[n-2],arr1[n-1])
    
elif len(misIndexList)==1:
    if arr1[n-2]==arr2[n-2]:
        misIndexList.append(arr1[n-1])
    else:
        misIndexList.append(arr1[n-2])    
    print(*misIndexList)
else:
    print(*misIndexList)

print("Time Complexity = O(n)")