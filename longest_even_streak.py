arr = [2, 4, 6, 3, 8, 10, 12, 14, 5, 6]

current_streak = 0
longest_streak = 0

for num in arr:
    if num % 2 == 0:
        current_streak += 1
        longest_streak = max(longest_streak, current_streak)
    else:
        current_streak = 0

print("Longest even streak:", longest_streak)
