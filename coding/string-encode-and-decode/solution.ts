const encode = (strs: string[]) => {
  const delimiter = "#";
  let res = "";

  for (let str of strs) {
    const len = str.length;
    res += `${len}${delimiter}${str}`;
  }

  return res;
};

const decode = (str: string) => {
  const res: string[] = [];
  let i = 0;

  while (i < str.length) {
    let j = i;
    while (str[j] !== "#") {
      j++;
    }
    const len = parseInt(str.slice(i, j));
    const startIndex = j + 1; // character after #
    const endIndex = startIndex + len;
    res.push(str.slice(startIndex, endIndex));
    i = endIndex;
  }

  return res;
};
