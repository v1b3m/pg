/**
 * Finds the k most frequent elements in an array using bucket sort.
 *
 * Bucket sort approach:
 * 1. First count frequencies of each number (O(n) time)
 * 2. Then create "buckets" where each index represents a frequency count
 *    - Index 1: numbers appearing once
 *    - Index 2: numbers appearing twice, etc.
 * 3. Finally, collect numbers from highest frequency buckets until we have k elements
 *
 * This achieves O(n) time complexity - better than sorting which would be O(n log n)
 */
const topKFrequent = (nums: number[], k: number) => {
  // Step 1: Count frequencies using a hash map
  const freqMap: Record<string, number> = {};
  for (let num of nums) {
    freqMap[num] = (freqMap[num] ?? 0) + 1;
  }

  // Step 2: Create frequency buckets
  const buckets: number[][] = [];
  for (let [num, freq] of Object.entries(freqMap)) {
    if (!buckets[freq]) {
      buckets[freq] = []; // Initialize bucket if it doesn't exist
    }
    buckets[freq].push(Number(num)); // Add number to its frequency bucket
  }

  // Step 3: Collect top k elements starting from highest frequency
  const result: number[] = [];
  for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
    if (buckets[i]) {
      // Add all numbers from this frequency bucket
      // Note: We might collect more than k elements here, but slice later
      result.push(...buckets[i]);
    }
  }

  // Return exactly k elements (in case last bucket pushed us over k)
  return result.slice(0, k);
};

// Test case
console.log(topKFrequent([1, 2, 2, 3, 3, 3], 2)); // [3, 2]
