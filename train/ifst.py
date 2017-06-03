a = 1
b = 3
if not(a == 1)or(b == 2):
    print(True)
elif b==2 and a ==0:
    print(False)
else:
    print("hi")
'''
This is a multiline
comment.
'''
#test
str = "hidsffsdvklfbs"
if "hi" in str:
    print("have")
print("\n")
for i in range(10):
    print(i)
print("\n")

for i in range(0,10,-1):
    print(i)
print("\n")
str = "abcd1234"
for i in range(len(str)):
    print(str[i])
print("\n")
for i in "abcd1234":
    print(i)
print("\n")
for i in {'cat','dog','tin'}:
    print(i)
print("\n")
for i in range(10):
    for j in range(i):
        print("*")
jj = {"ff":"tin"}
ii = {"tin":jj,'2':3}
check = "tin"
check2 = "ff"
if check in ii:
    print(ii[check])
    if check2 in ii[check]:
        print(jj[check2])
else:
    print("not")