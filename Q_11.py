###There are also several functions in pythio than can search for substrings

sampleStr = input("Enter string:  ")
subStr = input("Enter the substring to look for: ")
strLen = len(sampleStr)
subLen = len(subStr)

for i in range(strLen - subLen + 1):
    for j in range(subLen):
        if sampleStr[i + j] != subStr[j]:
            break

    if j +1  == subLen:
        print(i)
print("Time Complexity = O(n^2)")
