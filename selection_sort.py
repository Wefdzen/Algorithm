nums = [3, 1, 4, 7, 8, 5, 10, 6, 9, 2]

print("Was:", nums)

for i in range(len(nums)):
    lowest = i

    for j in range(i + 1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j

    nums[i], nums[lowest] = nums[lowest], nums[i]

print("Now:", nums)