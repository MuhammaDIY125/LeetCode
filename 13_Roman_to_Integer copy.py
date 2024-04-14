class RomanNumerals:
    rim_sonlar = [(1000, 'M'),
                  (900, 'CM'),
                  (500, 'D'),
                  (400, 'CD'),
                  (100, 'C'),
                  (90, 'XC'),
                  (50, 'L'),
                  (40, 'XL'),
                  (10, 'X'),
                  (9, 'IX'),
                  (5, 'V'),
                  (4, 'IV'),
                  (1, 'I')]

    @staticmethod
    def to_roman(self, s: str) -> int:
        son = 0
        for i, r in self.rim_sonlar:
            while s.startswith(r):
                son += i
                s = s[len(r):]
        return son
    
    @staticmethod
    def from_roman(roman_num : str) -> int:
        return 0

s1 = RomanNumerals()
print(s1.to_roman("MMXXII"))