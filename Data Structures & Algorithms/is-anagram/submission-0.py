class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        teen = {}
        if len(s)!= len(t):
            return False
        for i in s:
            seen[i] = seen.get(i,0)+1
            "how can i check both have same values or not"
        for j in t:
            teen[j] = teen.get(j,0)+1
        return seen ==teen


        