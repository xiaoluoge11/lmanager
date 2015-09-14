#!/usr/bin/env python
def mem():
    grains = {}
    f = open('/proc/meminfo')
    lines = f.readlines()
    f.close()
    num = lines[0].strip('\n').split(':')[1]
    total = int(num.split()[0])/1024
#    mem = {'total':num}
    grains['mem']=total
    return grains
if __name__ == '__main__':
    print mem()
