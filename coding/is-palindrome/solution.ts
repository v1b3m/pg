class PalindromeSolution {
  isPalindrome(s: string): boolean {
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
      left = this.skipNonAlphanumeric(s, left, right, 1);
      right = this.skipNonAlphanumeric(s, right, left, -1);

      if (left < right && s[left].toLowerCase() !== s[right].toLowerCase()) {
        return false;
      }

      left++;
      right--;
    }
    return true;
  }

  private skipNonAlphanumeric(
    s: string,
    index: number,
    bound: number,
    step: number
  ): number {
    while (index !== bound && !this.isAlphanumeric(s[index])) {
      index += step;
    }
    return index;
  }

  private isAlphanumeric(char: string): boolean {
    return /^[a-z0-9]$/i.test(char);
  }
}
