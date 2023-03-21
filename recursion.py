def hell(i):
    print(i)
    if i < 1:
        return 0
    else:
        hell(i - 1)


hell(4)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print("result fact:", fact(3))