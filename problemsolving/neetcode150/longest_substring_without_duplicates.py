class LongestSubstringWithoutDuplicates:

    # O(n) - But a bit complex and have bottleneck
    def sol1(self, s: str) -> int:
        if len(s) == 0:
            return 0

        hash_tbl, output, l, r = {}, 1, 0, 1
        hash_tbl[s[l]] = l
        while r < len(s):
            r_char = s[r]
            if r_char in hash_tbl:
                output = max(output, len(hash_tbl))
                l = hash_tbl[r_char] + 1
                r = l + 1
                hash_tbl.clear()
                hash_tbl[s[l]] = l
            else:
                hash_tbl[r_char] = r
                r += 1
        output = max(output, len(hash_tbl))
        return output

    # O(n) - optimized
    def sol2(self, s: str) -> int:
        res = 0
        l = 0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res
