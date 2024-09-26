// statisticsHelper.ts

/**
 * 配列の平均値を計算する
 * @param numbers 数値の配列
 * @returns 平均値
 */
export function calculateMean(numbers: number[]): number {
  if (numbers.length === 0) return 0;
  const sum = numbers.reduce((acc, val) => acc + val, 0);
  return sum / numbers.length;
}

/**
 * 配列の中央値を計算する
 * @param numbers 数値の配列
 * @returns 中央値
 */
export function calculateMedian(numbers: number[]): number {
  if (numbers.length === 0) return 0;
  const sorted = [...numbers].sort((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2