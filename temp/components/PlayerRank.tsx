import { Suspense } from 'react';
import { ArrowUp, ArrowDown, Minus } from 'lucide-react';
import { getPlayerRank, getRankHistory, getNextRankInfo } from '@/lib/rankUtils';
import type { PlayerRank, RankHistory, NextRankInfo } from '@/types';

async function PlayerRankContent({ userId }: { userId: string }) {
  const playerRank: PlayerRank = await getPlayerRank(userId);
  const rankHistory: RankHistory[] = await getRankHistory(userId);
  const nextRankInfo: NextRankInfo = await getNextRankInfo(userId);

  return (
    <div className="bg-white shadow-lg rounded-lg p-6 max-w-md mx-auto">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">プレイヤーランク</h2>
      
      <div className="mb-6">
        <p className="text-xl font-semibold text-gray-700">現在のランク: {playerR