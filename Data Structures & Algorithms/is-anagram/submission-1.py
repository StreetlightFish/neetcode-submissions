class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sarray = []
        tarray = []

        for letter in s:
            sarray.append(letter)
        sarray.sort()

        for letter in t:
            tarray.append(letter)
        tarray.sort()

        if sarray == tarray:
            return True
        return False