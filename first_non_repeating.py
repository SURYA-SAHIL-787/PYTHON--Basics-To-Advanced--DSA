def first_non_repeating_char(s):
    freq = {}

    # Count frequency of each character
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Find first character with frequency 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    return None


# Example usage
text = "aabbcddee"
result = first_non_repeating_char(text)

if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")
