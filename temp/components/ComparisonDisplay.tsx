import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';

type ComparisonDisplayProps = {
  playerSelection: number;
  averageSelection: number;
};

export default function ComparisonDisplay({ playerSelection, averageSelection }: ComparisonDisplayProps) {
  const [deviation, setDeviation] = useState(0);
  const [feedback, setFeedback] = useState('');

  useEffect(() => {
    const calculatedDeviation = playerSelection - averageSelection;
    setDeviation(calculatedDeviation);

    if (Math.abs(calculatedDeviation) <= 1) {
      setFeedback('あなたの選択は平均的です！');