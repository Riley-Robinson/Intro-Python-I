def mult2(n):
    return n * 2

num = 50

print(mult2(num))

def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2

nums = [10, 60, 4, 15]

mult2_list(nums)

print(nums)

def mult2_new_list(l):
    new_list = []
    for in in range(len(l)):
        new_list.append(l[i] * 2)

        return new_list

print(mult2_list([3, 5, 34, 10, 15]))