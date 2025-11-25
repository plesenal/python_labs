# mnen
nums = [[3, -1, 5, 5, 0], [42], [-5, -2, -9], [], [1.5, 2, 2.0, -3.1]]


def min_max(nums):
    if list:
        return (min(nums), max(nums))
    else:
        return "ValueError"


for i in nums:
    print(f"{i} -> {min_max(i)}")

nums = [[3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]]


def unique_sorted(nums):
    return sorted(list(set(nums)))


for i in nums:
    print(f"{i} -> {unique_sorted(i)}")

nums = [[[1, 2], [3, 4]], ([1, 2], (3, 4, 5)), [[1], [], [2, 3]], [[1, 2], "ab"]]


def flatten(mat):
    st_itog = []
    for i in list:
        if type(i) != str:
            for s in i:
                st_itog.append(s)
        else:
            return "TypeError"
    return st_itog


for i in nums:
    print(f"{i} -> {flatten(i)}")
