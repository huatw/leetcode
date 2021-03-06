# backtracking
class Solution:
    def permute(self, nums):
        res = []

        def dfs(rest, acc, seen):
            if not rest:
                res.append([*acc])
                return
            for i, num in enumerate(nums):
                if i not in seen:
                    seen.add(i)
                    acc.append(num)
                    dfs(rest - 1, acc, seen)
                    acc.pop()
                    seen.remove(i)

        dfs(len(nums), [], set())
        return res

# Iter
class Solution:
    def permute(self, nums):
        res = []
        stack = [([], nums)]
        while stack:
            acc, rest_ns = stack.pop()
            if not rest_ns:
                res.append(acc)
                continue
            for i, n in enumerate(rest_ns):
                stack.append((acc + [n], rest_ns[:i] + rest_ns[i + 1:]))
        return res


# DFS O(n2) O(n2)
class Solution:
    def permute(self, nums):
        res = []

        def dfs(ns, path):
            if not ns:
                res.append(path)
                return

            for i, n in enumerate(ns):
                dfs(ns[:i] + ns[i + 1:], path + [n])

        dfs(nums, [])
        return res

# def permute(nums):
#     def dfs(ns, acc):
#         if not ns:
#             return [acc]
#         res = []
#         for i, n in enumerate(ns):
#             res.extend(dfs(ns[:i] + ns[i + 1:], acc + [n]))
#         return res
#     return dfs(nums, [])


class Solution:
    def permute(self, nums):
        return map(list, itertools.permutations(nums))