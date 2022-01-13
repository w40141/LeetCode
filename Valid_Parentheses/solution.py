class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s) % 2 == 0:
            return False
        c: str = ""
        for p in s:
            if p == '(' or p == '[' or p == '{':
                c += p
            elif p == ')' or p == ']' or p == '}':
                if not c:
                    return False
                last: str = c[-1]
                if p == ')' and last == '(':
                    c = c[:-1]
                elif p == ']' and last == '[':
                    c = c[:-1]
                elif p == '}' and last == '{':
                    c = c[:-1]
                else:
                    return False
            else:
                return False
        if c:
            return False
        else:
            return True
