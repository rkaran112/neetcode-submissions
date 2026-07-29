class Solution:
    def isValid(self, s: str) -> bool:
        # 3 things same bracket valid, not same invalid, opening but no closing invalid
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif i == ")" or i == "}" or i == "]":
                if not stack:
                    return False
                if stack[-1] == "(" and i == ")":
                    stack.pop(-1)
                elif stack[-1] == "{" and i == "}":
                    stack.pop(-1)
                elif stack[-1] == "[" and i == "]":
                    stack.pop(-1)
                else:
                    return False
        return len(stack) ==0

            