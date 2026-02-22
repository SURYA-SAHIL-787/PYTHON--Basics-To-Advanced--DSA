nums = list(map(int, input("Enter numbers: ").split()))
even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Numbers:", nums)
print("Even count:", even)
print("Odd count:", odd)
