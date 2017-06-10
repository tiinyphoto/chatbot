go = "testgo"
i = 1

def a(v):
    return "pass",v

def dd(g,f):

    if type(g) is int:
        return "ddd p1",g+f+i

def dd(check,target):
    if isinstance(check, dict):
        if check in target:
          return target[check]
    elif isinstance(target,str):
        return target

if __name__ == '__main__':
    print (go)
    while True:
        d = dd("str",dict_target)
        if isinstance(d,str):
            print(d)