# O(n2)
class Solution:
    def solveNQueens(self, n):
        res = []

        def dfs(queens, level, path): # O(n2)
            if level == n:
                res.append(path)
                return

            for i in range(n): # O(n)
                queens[level] = i
                if check(queens, level):
                    dfs(queens, level + 1, path + ['.' * i + 'Q' + '.' * (n - i - 1)])


        def check(queens, level): # O(n)
            for i in range(level):
                if queens[i] == queens[level] or abs(queens[i] - queens[level]) == level - i:
                    return False
            return True


        dfs([None] * n, 0, [])
        return res
