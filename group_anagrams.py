def groupAnagrams(strs:list[str]) -> list[list[str]]:
    
    hash = {"".join(sorted(strs[0])):[strs[0]]}
    
    for i in range(1, len(strs)):
        s = "".join(sorted(strs[i]))
        if s in hash:
            hash[s].append(strs[i])
        else:
            hash.update({s:[strs[i]]})
    return list(hash.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))