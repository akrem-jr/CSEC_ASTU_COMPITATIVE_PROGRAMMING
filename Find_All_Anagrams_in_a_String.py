
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        pcount, scount = {}, {}
        for i in range(len(p)):
            pcount[p[i]] = 1 + pcount.get(p[i], 0)
            scount[s[i]] = 1 + scount.get(s[i], 0)

        res = [0] if pcount == scount else []
        left = 0

        for right in range(len(p), len(s)):
            scount[s[right]] = 1 + scount.get(s[right], 0)
            scount[s[left]] -= 1

            if scount[s[left]] == 0:
                scount.pop(s[left])

            if scount == pcount:
                res.append(left + 1)  # Append the starting index of the anagram

            left += 1

        return res
