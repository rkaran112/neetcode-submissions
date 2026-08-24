class Solution:
    def isValid(self, s: str) -> bool:
# if i is a opening bracked push it in stack,if i is a closing bracket,
# check if the top matches with the corresponding closing bracketg
        stack = []
        seen = {'}': '{', ']': '[', ')': '('}
        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            else:
                if not stack or stack.pop() != seen[i] :
                    return False
        return not stack