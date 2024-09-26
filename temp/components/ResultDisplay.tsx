import { FC } from 'react';
import { BowlSelection, Statistics, Feedback } from '../types';

interface ResultDisplayProps {
  playerSelection: BowlSelection;
  averageSelection: Statistics;
  feedback: Feedback;
}

const ResultDisplay: FC<ResultDisplayProps> = async ({ playerSelection, averageSelection, feedback }) => {
  const calculateDeviation = () => {
    return playerSelection.bowl_type - averageSelection.bowl_type;
  };

  const deviation = calculateDeviation();

  return (
    <div className="bg-white shadow-lg rounded-lg p-6 max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold mb-4 text-center text-gray-800">ゲーム結果</h2>

      <div className="mb-6">
        <h3 className="text-