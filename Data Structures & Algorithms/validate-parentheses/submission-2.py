class Solution:
    def isValid(self, s: str) -> bool:
        bracketmap =  {')':'(','}':'{',']':'['}
        stack = []

        for ch in s:
            if ch in bracketmap:
                if stack and stack[-1] == bracketmap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
