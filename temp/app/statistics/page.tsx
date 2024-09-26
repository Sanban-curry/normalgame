import { Suspense } from 'react';
import StatisticsChart from '@/components/StatisticsChart';
import PlayerComparison from '@/components/PlayerComparison';
import { getStatistics, getPlayerStats } from '@/app/api/statistics/route';

export const metadata = {
  title: '統計データ | NormaBowl',
  description: 'NormaBowlの統計データと平均値、トレンドを表示します。',
};

async function StatisticsContent() {
  const statistics = await getStatistics();
  const playerStats = await getPlayerStats();

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">統計データ</h1>
      
      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-4">全体の平均値とトレンド</h2>
        <div className="bg-white shadow-