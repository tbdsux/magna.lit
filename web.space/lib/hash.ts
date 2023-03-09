export const encodeChapter = (chapter: string) => {
  const buf = Buffer.from(chapter);

  return buf.toString("base64");
};

export const decodeChapter = (hash: string) => {
  const buf = Buffer.from(hash, "base64");

  return buf.toString("ascii");
};
