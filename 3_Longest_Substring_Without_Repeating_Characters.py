class Solution:
    def lengthOfLongestSubstring(self, s: str):
        s = set(s.split())
        print(s)
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