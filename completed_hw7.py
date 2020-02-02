f1 = open("/etc/passwd", "r")
f2 = open("/etc/group", "r")
uids = {x.split(":")[0]: x.split(":")[2]+":"+x.split(":")[6][:-1:] for x in f1.readlines()}
i = {}
for k in uids:
    k = uids[k].split(":")[1]
    if k in i:
        i[k] += 1
    else:
        i[k] = 1

for k in i:
    print(f"{k}:{i[k]} times")


for z in [x for x in [e.split(":")[0] + ":" + e.split(":")[3][:-1:] for e in f2.readlines()]]:
    if z.split(":")[1].split(",")[0] != "":
        print(z.split(':')[0], end=':')
        i = iter(z.split(':')[1].split(','))
        while True:
            try:
                print(uids[next(i)].split(":")[0], end="")
            except:
                print(end=" ")
                break
            print(end=",")
