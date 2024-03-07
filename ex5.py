def revertStr(s):
    arr = []
    for char in s:
        arr.append(char)
    
    str = ""

    for i in range(len(arr) - 1, -1, -1):
        str += arr[i]

    return str

strToRevert = input("String a ser revertida: ")

print(revertStr(strToRevert))