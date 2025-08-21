# REMOVE OUTERMOST PARENTHESIS

'''
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
'''

def removeOuterParenthesis(s):
    result = []
    count = 0
    
    for char in s:
        if char == '(':
            if count > 0:
                result.append(char)
            count += 1
        else:
            count -= 1
            if count > 0:
                result.append(char)
    
    return "".join(result)

# Examples
s1 = "(()())(())"
print(removeOuterParenthesis(s1)) # Output: "()()()"

# Additional examples
s2 = "(()())(())(()(()))"
print(removeOuterParenthesis(s2)) # Output: "()()()()(())"

s3 = "()()"
print(removeOuterParenthesis(s3)) # Output: ""

s4 = "(())"
print(removeOuterParenthesis(s4)) # Output: "()"

s5 = "((()))"
print(removeOuterParenthesis(s5)) # Output: "(())"

s6 = "((())())"
print(removeOuterParenthesis(s6)) # Output: "(())()"

s7 = "()(())"
print(removeOuterParenthesis(s7)) # Output: "()"

s8 = "(()(()))"
print(removeOuterParenthesis(s8)) # Output: "()(())"

s9 = "((()()))(())"
print(removeOuterParenthesis(s9)) # Output: "(()())()"

s10 = "((((()))))"
print(removeOuterParenthesis(s10)) # Output: "(((())))"