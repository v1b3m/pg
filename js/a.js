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

    for (const val of Object.keys(sMap)) {
      if (sMap[val] !== tMap[val]) return false;
    }

    return true;
  }
}
