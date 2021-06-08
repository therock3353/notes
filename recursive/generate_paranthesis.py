

def is_valid_parans(params):
    stack = []
    for paran in params:
        if paran == '(':
            stack.append(paran)
        elif paran == ')':
            if not stack:
                return False
            elif stack.pop() != '(':
                return False
    if stack:
        return False
    return True

def generate_paranthesis_rec(n, open, close, curr, result):
    if len(curr) == n:
        if is_valid_parans(curr):
            result.append("".join(curr))
            print "".join(curr)
        return result

    if open > close:
        return result
    if open > 0:
        result = generate_paranthesis_rec(n=n, open=open-1, close=close, curr=curr+['('], result=result)
    if close > 0:
        result = generate_paranthesis_rec(n=n, open=open, close=close-1, curr=curr+[')'], result=result)

    return result


def generate_paranthesis(n):
    if n == 0:
        return

    r = []
    generate_paranthesis_rec(n=2*n, open=n, close=n, curr=[], result=r)
    return r


if __name__=="__main__":

    i = 3
    print generate_paranthesis(i)