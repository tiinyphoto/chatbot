go = "testgo"
i = 1
def a(v) :
    return ("pass",v)
def dd(g,f):
    global i
    if type(g) is int:
        return ("ddd p1",g+f+i)
def dd(g):
    if isinstance(g, int):
        return ("ddd p2",g)

if __name__ == '__main__':
    global go
    print (go)