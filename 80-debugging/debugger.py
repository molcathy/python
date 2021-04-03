def num_doubler(nums):
    new_nums = []
    for num in nums:
        new_nums.append(num + num)
    return new_nums

def str_doubler(strings):
    new_strings = []
    for strg in strings:
        new_strings.append(strg + strg)
    return new_strings

def main():
    nd = num_doubler([1, 2, 3])
    sd = str_doubler(["a", "b", "c"])

    print(nd)
    print(sd)

if __name__ == "__main__":
    main()