class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countt, window = {}, {}
        
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        
        have, need = 0, len(t)
        res, reslen = [-1, -1], float("inf")
        left = 0
        
        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)
            
            if s[right] in countt and window[s[right]] == countt[s[right]]:
                have += 1
            
            while have == need:
                if (right - left) < reslen:
                    res = [left, right]
                    reslen = (right - left + 1)
                
                window[s[left]] -= 1
                
                if s[left] in countt and window[s[left]] < countt[s[left]]:
                    have -= 1
                
                left += 1

        if reslen != float("inf"):
            return s[res[0]: res[1] + 1]
        else:
            return ""
