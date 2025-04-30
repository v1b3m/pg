/**
 * Finds two numbers in an array that add up to the target.
 * @param nums - Array of numbers
 * @param target - Target sum
 * @returns Array of two indices whose values sum to target
 *
 * Time Complexity: O(n) - Single pass through the array
 * Space Complexity: O(n) - Stores numbers in a hash map
 */
const twoSum = (nums: number[], target: number): number[] => {
  const numMap = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const difference = target - nums[i];
    if (numMap.has(difference)) {
      return [numMap.get(difference)!, i];
    }
    numMap.set(nums[i], i);
  }

  throw new Error("No two sum solution found");
};

// Test cases
console.log(twoSum([3, 4, 5, 6], 7)); // [0, 1]
console.log(twoSum([4, 5, 6], 10)); // [0, 2]
console.log(twoSum([5, 5], 10)); // [0, 1]
