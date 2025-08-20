def isAnagram(s: str, t: str) -> bool:
    if (s) == sorted(t):
        return True
    return False

print(isAnagram("racecar", "carrace"))
print(isAnagram("jar", "jam"))
print(isAnagram("a", "aa"))