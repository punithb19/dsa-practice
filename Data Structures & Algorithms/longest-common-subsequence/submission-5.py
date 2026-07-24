class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        cache = {}

        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]

            if i>=n or j>=m:
                return 0
            
            if text1[i]==text2[j]:
                ans =  1+dfs(i+1, j+1)
                cache[(i,j)] = ans
                return ans
            
            ans = max(dfs(i,j+1), dfs(i+1, j))
            cache[(i,j)] = ans
            return ans

        return dfs(0,0)