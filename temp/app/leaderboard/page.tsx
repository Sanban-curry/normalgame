// app/leaderboard/page.tsx

import { Suspense } from 'react';
import LeaderboardTable from '@/components/LeaderboardTable';
import PlayerRank from '@/components/PlayerRank';

async function getLeaderboardData() {
  // API経由でデータを取得（実際の実装ではここでAPIを呼び出します）
  const res = await fetch('http://localhost:3000/api/leaderboard', { cache: 'no-store' });
  if (!res.ok) {
    throw new Error('Failed to fetch leaderboard data');
  }
  return res.json();
}

export default async function LeaderboardPage() {
  const leaderboardData = await getLeaderboardData();

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">NormaBowl リーダーボード</h1>