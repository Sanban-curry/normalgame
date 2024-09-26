// PlayerComparison.tsx

import { FC } from 'react';

interface PlayerComparisonProps {
  playerScore: number;
  averageScore: number;
  percentile: number;
  rank: number;
  totalPlayers: number;
}

const PlayerComparison: FC<PlayerComparisonProps> = async ({
  playerScore,
  averageScore,
  percentile,
  rank,
  totalPlayers,
}) => {
  const maxScore = Math.max(playerScore, averageScore);
  const playerBarWidth = (playerScore / maxScore) * 100;
  const averageBarWidth = (averageScore / maxScore) * 100;

  return (
    <div className="bg-white shadow-lg rounded-lg p-6 max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold mb-4