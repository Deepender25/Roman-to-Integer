# 🏛️ Roman to Integer

This repository contains a Python solution for the **"Roman to Integer"** problem from LeetCode.

---

## 📘 Problem Description

Given a Roman numeral, convert it to an integer.

Roman numerals are represented by the following symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are typically written from largest to smallest from left to right. However, if a smaller value appears before a larger one, it is subtracted.

### Examples

```
Input: "III"
Output: 3

Input: "IV"
Output: 4

Input: "IX"
Output: 9

Input: "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4
```

---

## 🚀 Approach

1. Convert each Roman character into its corresponding integer using a dictionary.
2. Traverse the list of integers and apply subtraction logic:
   - If a value is smaller than the one following it, subtract it from the next and set the current value to 0.
3. Return the sum of the modified list.

---

## 🧠 Python Solution

```python
class Solution(object):
    def romanToInt(self, s):
        n = []
        li = [str(i) for i in s]
        ref = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in li:
            n.append(ref[i])
        for i in range(len(n)-1):
            if n[i] < n[i+1]:
                n[i+1] = n[i+1] - n[i]
                n[i] = 0
        return sum(n)
```

---

## ▶️ How to Run

```python
sol = Solution()
print(sol.romanToInt("MCMXCIV"))  # Output: 1994
```

---

## ⏱️ Complexity

- **Time Complexity**: O(n), where `n` is the length of the input string.
- **Space Complexity**: O(n), for storing converted integers.

---

## 📎 Related Topics

- String Manipulation
- Hash Maps
- Greedy Algorithms

---

## 🔗 LeetCode Link

👉 [Roman to Integer – LeetCode](https://leetcode.com/problems/roman-to-integer/)
