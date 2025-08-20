def isPalindrome(s: str) -> bool:
    allowed = set(list("qwertyuiopasdfghjklzxcvbnm1234567890"))
    arr = []
    for i in range(0, len(s)):
        if s[i].lower() in allowed:
            arr.append(s[i].lower())
    front = 0
    back = len(arr) - 1
    for i in range(0, len(arr)//2):
        if arr[front] == arr[back]:
            front += 1
            back -= 1
        else:
            return False
    return True


print(isPalindrome("0P"))