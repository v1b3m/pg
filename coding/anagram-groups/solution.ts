function groupAnagrams(strs: string[]): string[][] {
  const map = new Map<string, string[]>();

  for (const str of strs) {
    const count = new Array(26).fill(0);
    for (const char of str) {
      const idx = char.charCodeAt(0) - "a".charCodeAt(0);
      count[idx] += 1;
    }
    const key = count.join(",");
    map.set(key, [...(map.get(key) ?? []), str]);
  }

  return Array.from(map.values());
}
