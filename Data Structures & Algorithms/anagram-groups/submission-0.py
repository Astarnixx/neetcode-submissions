class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            mp[sortedS].append(s)
        return list(mp.values())