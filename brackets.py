from collections import deque

def brackets(line):
    bracketss = {']': '[', ')': '(', '}': '{'}
    st = deque()
    for i in line:
        if i in '[({':
            st.append(i)
        if i in '])}':
            if len(st):
                i = bracketss[i]
                if i != st.pop():
                    return False
            else:
                return False
    if len(st):
        return False
    return True

line = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"
print(brackets(line))