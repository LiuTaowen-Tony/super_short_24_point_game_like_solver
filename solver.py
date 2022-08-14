def split2(lst):
    for i in range(len(lst)):
        for j in range(i):
            nlst = lst.copy()
            yield (nlst.pop(i), nlst.pop(j), nlst)

calcs = {'+': lambda a,b: a+b, '-': lambda a,b: a-b, '*': lambda a,b: a*b,
        '/': lambda a,b: a/b, 'r-': lambda a,b: b-a, 'r/': lambda a,b: b/a}

def solve(lst, k):
    if len(lst) == 1: return abs(lst[0] - k) < 1e-6
    for x, y, nlst in split2(lst):
        for name, calc in calcs.items():
            try: result = calc(x, y)
            except ZeroDivisionError: continue
            if solve(nlst + [result], k):
                print(f'{x} {name} {y} = {result}')
                return True
    return False
