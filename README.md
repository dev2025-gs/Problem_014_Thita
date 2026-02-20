# String Compression

## 📝 Problem Description

Given an array of characters `chars`, compress it using the following algorithm:

1. Begin with an empty string `s`.
2. For each group of consecutive repeating characters in `chars`:
   - If the group's length is **1**, append the character to `s`.
   - Otherwise, append the character followed by the group's length.

The compressed string `s` **must not** be returned separately. Instead, it must be stored **in-place** inside the input array `chars`.

If a group’s length is **10 or greater**, its digits must be split into separate characters in the array.

After modifying the input array, return the **new length** of the array.
(https://thita.ai/problems/string-compression)

> ⚠️ You must write an algorithm that uses only **constant extra space (O(1))**.

---

## 📌 Examples

### Example 1

**Input:**
chars = ["a","a","b","b","c","c","c"]


**Output:**
Return 6
chars = ["a","2","b","2","c","3"]


**Explanation:**

- Groups: `"aa"`, `"bb"`, `"ccc"`
- Compressed string: `"a2b2c3"`
- New length: `6`

---

### Example 2

**Input:**
chars = ["a"]


**Output:**
Return 1
chars = ["a"]


**Explanation:**

- Group: `"a"`
- Single characters are not compressed.

---

### Example 3

**Input:**
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]


**Output:**
Return 4
chars = ["a","b","1","2"]


**Explanation:**

- Groups: `"a"`, `"bbbbbbbbbbbb"`
- `"bbbbbbbbbbbb"` has length `12`
- Compressed string: `"ab12"`
- Digits `"1"` and `"2"` are stored separately.

---

## 🔒 Constraints

- `1 <= chars.length <= 2000`
- `chars[i]` can be:
  - Lowercase English letter
  - Uppercase English letter
  - Digit
  - Symbol

---

## 💡 Key Requirements

- Modify the input array **in-place**
- Use **O(1) extra space**
- Return the **new length**
- Do not allocate another array for compression

---

## 🧠 Approach Overview

A common approach to solving this problem efficiently:

- Use two pointers:
  - A **read pointer** to scan through the array
  - A **write pointer** to overwrite compressed characters
- Count consecutive repeating characters
- Write:
  - The character
  - The count (if greater than 1), digit by digit

This ensures:

- Linear time complexity: **O(n)**
- Constant space complexity: **O(1)**

---

## 🚀 Summary

This problem tests your understanding of:

- Two-pointer techniques
- In-place array modification
- Careful handling of multi-digit numbers
- Space optimization

Efficiently compressing the array while respecting constant space constraints is the core challenge of this problem.

