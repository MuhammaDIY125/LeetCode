class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lst = []
        s = set(s.split())
        if s == set():
            return 1
        if len(s) == 1:
            maximum = 0
        else:
            maximum = 1
        for q in s:
            for i in range(len(q)):
                st = ""
                for j in q[i:]:
                    if j not in st:
                        st += j
                    else:
                        lst.append(st)
                        st = j
                lst.append(st)
        maximum += len(max(lst, key=lambda x: len(x)))
        return maximum
print(Solution().lengthOfLongestSubstring(input()))