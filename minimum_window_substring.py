from collections import Counter


def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    target_count = Counter(t)
    window_count = {}
    have = 0
    need = len(target_count)

    left = 0
    result = [-1, -1]
    result_length = float("inf")

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in target_count and window_count[char] == target_count[char]:
            have += 1

        while have == need:
            if (right - left + 1) < result_length:
                result = [left, right]
                result_length = right - left + 1

            window_count[s[left]] -= 1
            if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
                have -= 1

            left += 1

    left, right = result
    return s[left:right + 1] if result_length != float("inf") else ""


s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))
