# __Author__ __Lencof__
# sorted_nums.py

def sorted(nums):
    s = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

random_list_of_nums = [5, 2, 1, 4, 6]
sorted(random_list_of_nums)
print(random_list_of_nums)
