#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    return int(str(some_int)[-8:])


def optimized_fibonacci(i):
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


class SummableSequence(object):
    def __init__(self, *initials):
        self.initials = list(initials)

    def __call__(self, i):
        if i <= len(self.initials) - 1:
            return self.initials[i]

        nums = self.initials[:]
        for j in range(len(self.initials), i + 1):
            nums.append(sum(nums))
            if j != i:
                nums.pop(0)
        return nums[-1]


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
