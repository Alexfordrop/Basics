def twotermswithsumx(nums, x):
    for i in range(len(nums)):
        for j in range(i + l, len(nums)):
            if nums[i] + num[j] == x:
                return nums[i], nums[j]
    return 0, 0