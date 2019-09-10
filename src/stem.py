
class PorterStemmer:
    def __init__(self):
        self.vowels = ('a', 'e', 'i', 'o', 'u')

    def is_consonant(self, s: str, i: int):
        return not self.is_vowel(s, i)

    def is_vowel(self, s: str, i: int):
        if s[i].lower() in self.vowels:
            return True
        elif s[i].lower() == 'y':
            if self.is_consonant(s, i-1):
                return True
            else:
                return False

    def find_m(self, s):
        i = 0
        m = 0
        while i < len(s):
            if self.is_vowel(s, i) and self.is_consonant(s, i+1):
                m += 1
                i += 2
            else:
                i += 1
        return m

    def contains_vowel(self, s):
        for v in self.vowels:
            if v in s:
                return True

        for i in range(len(s)):
            if s[i] == 'y':
                if self.is_vowel(s, i):
                    return True

        return False

    def ends_in_dub_const(self, s):
        if s[-2].lower() == s[-1].lower():
            if self.is_consonant(s, -1):
                return True

        return False

    def ends_cvc(self, s):
        if self.is_consonant(s, -1):
            if self.is_vowel(s, -2):
                if self.is_consonant(s, -3):
                    if s[-1] not in ('w', 'x', 'y'):
                        return True

        return False

    def step1a(self, s):
        if s[-4:].lower() == 'sses':
            s = s[:-4] + 'ss'
        elif s[-3:].lower() == "ies":
            s = s[:-3] + "i"
        elif s[-2:].lower() == "ss":
            pass
        elif s[-1].lower() == "s":
            s = s[:-1]
        return s

    def step1b(self, s):
        if s[-3:].lower() == 'eed':
            m = self.find_m(s[:-3])
            if m > 0:
                s = s[:-1]
        elif s[-2:].lower() == 'ed':
            if self.contains_vowel(s[:-2]):
                s = s[:-2]
                s = self.step1ba(s)
        elif s[-3:].lower() == 'ing':
            if self.contains_vowel(s[:-3]):
                s = s[:-3]
                s = self.step1ba(s)

        return s

    def step1ba(self, s):
        if s[-2:].lower() == 'at':
            s = s + 'e'
        elif s[-2:].lower() == 'bl':
            s = s + 'e'
        elif s[-2:].lower() == 'iz':
            s = s + 'e'
        elif self.ends_in_dub_const(s) and s[-1].lower() not in ('l', 's', 'z'):
            s = s[:-1]
        elif self.find_m(s) == 1 and self.ends_cvc(s):
            s += 'e'

        return s

    def __call__(self, s: str):
        s = self.step1a(s)
        s = self.step1b(s)
        return s
