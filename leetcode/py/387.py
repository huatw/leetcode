class Solution:
    def firstUniqChar(self, s):
        ch_cnt  = collections.Counter(s)
        for i, ch in enumerate(s):
            if ch_cnt[ch] == 1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s):
        ch_map = collections.defaultdict(list)

        for i, ch in enumerate(s):
            ch_map[ch].append(i)

        single_idxs = [idx_arr[0] for ch, idx_arr in ch_map.items() if len(idx_arr) == 1]

        return min(single_idxs) if single_idxs else -1
