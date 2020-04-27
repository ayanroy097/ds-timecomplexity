n = int(input())
# TC = O(1)

arr1 = list(map(str, input().split()[:n]))
# TC = O(n)

arr2 = list(map(str, input().split()[:n-1]))
# TC = O(n-1)
misIndex = 0
for i in range(n-1):
    if arr1[i] != arr2[i]:
        misIndex = i
        break
# TC = O(n-1)
if misIndex == 0:
    print(arr1[n-1])

else:
    print(arr1[misIndex])
 
print(f"Time Complexity = O(1)+3*O(n) = O(n)")