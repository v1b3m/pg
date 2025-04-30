const isAnagram = (s: string, t: string): boolean => {
  if (s.length !== t.length) return false;

  const freq = new Array(26).fill(0);
  const aCode = "a".charCodeAt(0);

  for (let i = 0; i < s.length; i++) {
    freq[s.charCodeAt(i) - aCode]++;
    freq[t.charCodeAt(i) - aCode]--;
  }

  return freq.every((count) => count === 0);
};

console.log(isAnagram("racecar", "carrace"));
console.log(isAnagram("jar", "jam"));
