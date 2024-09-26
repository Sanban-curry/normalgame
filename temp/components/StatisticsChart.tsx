'use client';

import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  ChartOptions,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

type DataPoint = {
  date: string;
  average: number;
  trend: number;
};

const StatisticsChart: React.FC = () => {
  const [chartData, setChartData] = useState<DataPoint[]>([]);

  useEffect(() => {
    // 実際のアプ