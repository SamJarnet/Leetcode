def isValid( s: str) -> bool:
    open_count = 0
    close_count = 0
    arr = []
    open = set(["{", "(", "["])
    def check(o, c):
        if o == "{" and c == "}":
            return True
        elif o == "(" and c == ")":
            return True
        elif o == "[" and c == "]":
            return True
        return False
    
    for i in range(0, len(s)):
        if s[i] in open:
            open_count += 1
        else:
            close_count += 1
        arr.append(" ")

    head = 0
    for i in range(0, len(s)):
        if s[i] in open:
            arr[head] = s[i]
            head += 1

        else:
            if s[i] not in open:
                if check(arr[head-1], s[i]):
                    arr[head-1] = " "
                    head -= 1
                else:
                    return False
    if close_count != open_count:
        return False
    return True
    


print(isValid("([]){"))