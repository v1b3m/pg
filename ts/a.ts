class Solution {
  /**
   * @param {string} s
   * @param {string} t
   * @return {boolean}
   */
  isAnagram(s, t) {
    if (s.length !== t.length) return false;

    const sMap = {};
    const tMap = {};

    for (let i in s) {
      sMap[s[i]] = (sMap[s[i]] ?? 0) + 1;
      tMap[t[i]] = (tMap[t[i]] ?? 0) + 1;
    }

    const joinedValues = (obj: Record<string, number>) =>
      Object.values(obj).join("");

    return joinedValues(sMap) === joinedValues(tMap);
  }
}
