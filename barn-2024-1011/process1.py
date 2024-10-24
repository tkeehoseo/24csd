def target_func(x):
    return float(x)**2+1.0

while True:
    try:
        l1 = [ x for x in input().split(',') ]
        if len(l1) == 1 and l1[0] == '':
            break
        l2 = [target_func(x) for x in l1]
    except ValueError:
        continue
    except EOFError:
        break
    for i in range(len(l2)):
        print(l2[i], end=',' if i !=len(l2)-1 else '\n')
