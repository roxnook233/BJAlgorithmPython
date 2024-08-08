#BJ 4949

while True:
    s = input()
    slb = srb = blb = brb = 0
    balanced = True
    stack =[]
    if(s[0] == '.'): break
    for c in s:
        if(c == '('): stack.append(c)
        elif c == '[': stack.append(c)
        elif c == ']':
            if (len(stack) == 0 or stack.pop() != '['): 
                balanced = False
                break
        elif c == ')':
            if (len(stack) == 0 or stack.pop() != '('):
                balanced = False
                break
        
    if len(stack) == 0 and balanced: print("yes")
    else: print("no")
