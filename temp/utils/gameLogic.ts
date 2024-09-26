// gameLogic.ts

import { BowlType, StatisticsData, FeedbackMessage } from '../types';

// プレイヤーの選択と統計データを比較する関数
export function compareSelection(playerSelection: BowlType, statistics: StatisticsData): number {
  const averageBowlType = calculateAverageBowlType(statistics);
  return Math.abs(playerSelection - averageBowlType);
}

// 統計データから平均のお茶碗タイプを計算する関数
function calculateAverageBowlType(statistics: StatisticsData): number {
  const totalSelections = statistics.reduce((sum, stat) => sum + stat.count, 0);
  const weightedSum = statistics.reduce((sum, stat) => sum + stat.bowlType * stat.count, 0);
  return weight    type: 'perfect',
      message: '完璧です！あなたの「普通」は社会の平