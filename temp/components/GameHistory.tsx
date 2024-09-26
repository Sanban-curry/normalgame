import { useState } from 'react';
import { ChevronDown, ChevronUp } from 'lucide-react';

type GameResult = {
  id: string;
  date: string;
  score: number;
  ranking: number;
};

async function getGameHistory(): Promise<GameResult[]> {
  // ここでデータベースからゲーム履歴を取得する処理を実装
  // この例では仮のデータを返します
  return [
    { id: '1', date: '2023-05-01', score: 85, ranking: 120 },
    { id: '2', date: '2023-05-03', score: 92, ranking: 50 },
    { id: '3', date: '2023-05-05', score: 78, ranking: 200 },
    // ... 他のゲーム結果
  ];