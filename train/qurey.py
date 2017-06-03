jj = {"ff":"tin"}
dict_target = {"tin":jj,'2':3}
def dd(check, target):
    if target is None:
        return False
    if isinstance(target, dict):
        if check in target:
            return target[check]
    elif isinstance(target, str):

        return target

def check(word):
    d = dd(word, dict_target)
    while True:
        if d is None:
            arg2 = input("need more:")
            d = dd(arg2, temp)
        if isinstance(d, str):
            return d
        else:
            temp = d
            d = dd(word,d)
if __name__ == '__main__':
    print(check("tin"))