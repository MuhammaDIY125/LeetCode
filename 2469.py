class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius+273.15, celsius*9/5+32]

s1 = Solution()
celsius = 36.50
print(s1.convertTemperature(celsius))