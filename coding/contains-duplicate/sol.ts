/**
 * Checks if an array contains any duplicate values.
 * @param nums - Array of numbers to check
 * @returns true if any value appears more than once, false otherwise
 */
const containsDuplicate = (nums: number[]): boolean => {
  const seen = new Set<number>();
  for (const num of nums) {
    if (seen.has(num)) return true;
    seen.add(num);
  }
  return false;
};

// Test cases
console.log(containsDuplicate([1, 2, 3, 4, 5, 1])); // true
console.log(containsDuplicate([1, 2, 3, 4])); // false
