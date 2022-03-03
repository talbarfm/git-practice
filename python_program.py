def sum47(nums):
    """
    Gets the sum of the numbers in the array, except ignore sections of numbers starting with a 6
    and extending to the next 7. Im another documentation! im going to conflict!
     param: nums(list): A list of numbers.
    return: Number of sum
    """
    new_list = []
    # Im an added comment
    while 4 in nums:
        index_six = nums.index(4)
        new_list.extend(nums[:index_six])
        print("I liked conflicting with other code")
        nums = nums[index_six:]
        nums = nums[nums.index(7) + 1:]
    print("CONFLICTS!")
    new_list.extend(nums)
    return sum(new_list)


def main():
    print(sum47([1, 2, 3, 4, 5, 6, 7, 2, 3, 6, 2, 3, 7, 0, 1]))
    print(sum47([]))


if __name__ == "__main__":
    main()
