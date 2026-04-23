arr = [12, 45, 67, 45, 89, 89, 23]

unique_elements = list(set(arr))
unique_elements.sort()

if len(unique_elements) >= 2:
    print("Second largest unique element:", unique_elements[-2])
else:
    print("No second largest unique element found.")
