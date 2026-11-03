class Solution:
    def isValid(self, s: str) -> bool:
        tracker = []
        lookup = { ")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in lookup:
                if tracker and tracker[-1] == lookup[c]:
                    tracker.pop()
                else:
                    return False
            else:
                tracker.append(c)

        return True if not tracker else False