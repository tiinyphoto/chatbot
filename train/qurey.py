
wifidic = {"เข้าไม่ได้":"ปิดเปิดใหม่","เชื่อมไม่ได้้":"ปิดเปิดใหม่","ต่อไม่ติด":"ปิดเปิดใหม่"}
landic ={"เข้าไม่ได้":"ถอดเสียบใหม่","เชื่อมไม่ได้้":"ถอดเสียบใหม่","ต่อไม่ติด":"ถอดเสียบใหม่"}
internetdic = {"wifi":wifidic,'lan':landic}
dict_target = {"internet":internetdic,"wifi":wifidic,'lan':landic}
def dd(check, target):
    if target is None:
        return False
    if isinstance(target, dict):
        if check in target:
            return target[check]
    elif isinstance(target, str):
        return target
def check(word,target):
    d = dd(word, target)
    temp = d

    while True:

        if d is False:
            return "กรุณาติดต่อเจ้าหน้าที่"
        if d is None:
            arg2 = input("ขอรายละเอียดเพิ่มเติ่ม: ")
            d = dd(arg2, temp)
        if isinstance(d, str):
            return d
        else:
            if isinstance(d,dict):
                temp = d
                d = dd(word,d)
if __name__ == '__main__':
    x = input("มีปัญหาเกี่ยวกับอะไร : ")
    print(check(x,dict_target))