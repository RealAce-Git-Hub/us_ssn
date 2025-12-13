def fun(m):
    cnt = 1
    while cnt <= 5:
        yield cnt
        cnt += 1

ctr = fun(5)
for i in ctr:
    print(i)