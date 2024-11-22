class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        opdict = defaultdict(list)
        for i in strs:
            isorted = ''.join(sorted(i))
            opdict[isorted].append(i)

        return list(opdict.values())