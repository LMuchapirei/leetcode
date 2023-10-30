def evalRPN(tokens):
    stack = []
    for c in tokens:
        if c == "+":
            a,b= stack.pop(),stack.pop()
            res = b + a
            stack.append(res)
        elif c == "*":
            a,b= stack.pop(),stack.pop()
            res = b * a
            stack.append(res)
        elif c == "/":
            a,b= stack.pop(),stack.pop()
            res = int(b/a)  # The trick to do division in python and then truncate to zero
            stack.append(res)
        elif c == "-":
            a,b= stack.pop(),stack.pop()
            res = b - a
            stack.append(res)
        else:
            stack.append(int(c))
    return stack[0]

    # A verbose way to achieve the same effect and not so efficient also beats only 5%
    # while len(tokens) > 1:
    #     for index in range(0,len(tokens)):
    #         val = tokens[index]
    #         if str.isdigit(val) or val.lstrip('-+').isdigit():
    #             continue
    #         else:
    #             if val == "+":
    #                 print(tokens)
    #                 tokens.pop(index)
    #                 a,b=tokens[index-1],tokens[index-2]
    #                 res= int(b)+ int(a)
    #                 print(tokens)
    #                 tokens.insert(index-2,str(res))
    #                 tokens.pop(index)
    #                 tokens.pop(index-1)
    #                 break
    #             elif val == "-":
    #                 print(tokens)
    #                 tokens.pop(index)
    #                 a,b=tokens[index-1],tokens[index-2]
    #                 res= int(b) - int(a)
    #                 print(tokens)
    #                 tokens.insert(index-2,str(res))
    #                 tokens.pop(index)
    #                 tokens.pop(index-1)
    #                 # tokens.insert(0,str(res))
    #                 break
    #             elif val =="*":
    #                 print(tokens)
    #                 tokens.pop(index)
    #                 a,b=tokens[index-1],tokens[index-2]
    #                 res= int(b) * int(a)
    #                 tokens.insert(index-2,str(res))
    #                 tokens.pop(index)
    #                 tokens.pop(index-1)
    #                 # tokens.insert(0,str(res))
    #                 break
    #             if val == "/":
    #                 print(tokens)
    #                 tokens.pop(index)
    #                 a,b=tokens[index-1],tokens[index-2]
    #                 res= int(int(b) / int(a))
    #                 print(tokens)
    #                 tokens.insert(index-2,str(res))
    #                 tokens.pop(index)
    #                 tokens.pop(index-1)
    #                 # tokens.insert(0,str(res))
    #                 break
    # return int(tokens[0])


# evalRPN(["2","1","+","3","*"])
# evalRPN(["4","13","5","/","+"])
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))