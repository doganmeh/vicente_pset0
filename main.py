import io
from contextlib import redirect_stdout


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
        if j == i:
            return z
        x = y
        y = z


def fibonacci_arr(i):
    if i == 0:
        return 0
    if i == 1:
        return 1

    nums = [0, 1]
    for j in range(2, i + 1):
        nums.append(sum(nums))
        if j == i:
            return nums[-1]
        nums.pop(0)


def summable(i, *initials):
    initials = list(initials)
    if i <= len(initials) - 1:
        return initials[i]

    nums = initials[:]
    for j in range(len(initials), i + 1):
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


def print_pyramid(rows):
    width = 2 * rows - 1
    for row in range(1, rows + 1):
        double = 2 * row - 1
        single = (width - double) // 2
        print('-' * single + '=' * double + '-' * single)


rows = 2
expected = '''-=-
===
'''
f = io.StringIO()
with redirect_stdout(f):
    print_pyramid(rows)
output = f.getvalue()
if not output == expected:
    print('expected')
    print(expected)
    print('but got')
    print(output)

rows = 3
expected = '''--=--
-===-
=====
'''
f = io.StringIO()
with redirect_stdout(f):
    print_pyramid(rows)
output = f.getvalue()
if not output == expected:
    print('expected')
    print(expected)
    print('but got')
    print(output)
