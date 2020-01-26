def fibonacci_rec(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    else:
        return fibonacci_rec(i - 1) + fibonacci_rec(i - 2)


def fibonacci(i):
    if i == 0:
        return 0
    if i == 1:
        return 1

    x = 0
    y = 1
    for j in range(2, i + 1):
        z = x + y
        if j != i:
            x = y
            y = z
    return z


def fibonacci_arr(i):
    if i == 0:
        return 0
    if i == 1:
        return 1

    nums = [0, 1]
    for j in range(2, i + 1):
        nums.append(sum(nums))
        if j != i:
            nums.pop(0)
    return nums[-1]


def summable(i, *args):
    args = list(args)
    if i <= len(args)-1:
        return args[i]

    nums = args[:]
    for j in range(len(args), i+1):
        nums.append(sum(nums))
        if j != i:
            nums.pop(0)
    return nums[-1]

# summable(10, 0, 1)

for i in range(40):
    print(i, fibonacci(i))
    print(i, summable(i, 0, 1))
#     # print(i, fibonacci_arr(i))
#     # print(i, fibonacci_rec(i))

# print(fibonacci_rec(35))
# print(fibonacci(35))
