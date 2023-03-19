nums = [2, 1, 5, 4, 7, 6]
nums.sort()
search_for = 7
print(nums)

lowest = 0
highest = len(nums) - 1
index = None  # future search index

while(lowest <= highest) and (index is None):
    mid = (lowest + highest) // 2  # middle\

    if nums[mid] == search_for:
        index = mid
    else:
        if search_for < nums[mid]:
            highest = mid - 1
        else:
            lowest = mid + 1

print("search for:", search_for, "index:", index)
