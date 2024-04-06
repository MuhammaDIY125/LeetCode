class Solution:
    def myAtoi(self, s: str) -> int:
        natija = ""
        z = 1
        lampochka = True
        if s:
            while s[0] == " ":
                s = s[1:]
            for i, value in enumerate(s):
                if (value == '+' or value == '-') and not i:
                    if value == '-':
                        z = -1
                elif value.isdigit():
                    natija += value
                else:
                    break
        if natija:
            natija = int(natija) * z
            if -2147483648 > natija:
                return -2147483648
            elif natija > 2147483647:
                return 2147483647
            else:
                return natija
        return 0

s1 = Solution()
print(s1.myAtoi("words and 987"))