Valid Palindrome
================

Solved

Easy

Given a string `s`, return `true` if it is a **palindrome**, otherwise return `false`.

A **palindrome** is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

**Example 1:**

    Input: s = "Was it a car or a cat I saw?"
    
    Output: true
    

Copy

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

**Example 2:**

    Input: s = "tab a cat"
    
    Output: false
    

Copy

Explanation: "tabacat" is not a palindrome.

**Constraints:**

* `1 <= s.length <= 1000`
* `s` is made up of only printable ASCII characters.

Recommended Time & Space Complexity

You should aim for a solution with `O(n)` time and `O(1)` space, where `n` is the length of the input string.

Hint 1

A brute force solution would be to create a copy of the string, reverse it, and then check for equality. This would be an `O(n)` solution with extra space. Can you think of a way to do this without `O(n)` space?

Hint 2

Can you find the logic by observing the definition of pallindrome or from the brute force solution?

Hint 3

A palindrome string is a string that is read the same from the start as well as from the end. This means the character at the start should match the character at the end at the same index. We can use the two pointer algorithm to do this efficiently.
