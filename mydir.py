import os

def mysearchfile(folder,filename):
    l = os.dir(folder)
    r = None
    for i in l:
        if i == folder:
            r = mysearchfile(i,filename)
        else:
            continue
    return r

print( mysearchfile('D:\\','hello.c'))
