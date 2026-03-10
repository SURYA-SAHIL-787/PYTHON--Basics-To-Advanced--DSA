def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i

    return [-1, -1]


# Example usage
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print("Indices:", result)
