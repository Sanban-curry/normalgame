'use client';

import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { Info } from 'lucide-react';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

type StatData = {
  bowlType: number;
  count: number;
};

const StatsDisplay: React.FC = () => {
  const [stats, setStats] = useState<StatData[]>([]);
  const [filteredStats, setFilteredStats] = useState<StatData[]>([]);
  const [filter, setFilter] = useState('all');

  useEffect(() => {
    // 実際のアプリケーションではここでAPIからデータを取得します
    const dummyData: StatData[] = [
      { bowlType: 1, count: 150 },
      { bowlType: 2, count: