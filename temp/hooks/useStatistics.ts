'use client';

import { useState, useEffect } from 'react';
import { supabase } from '@/lib/supabase';

interface BowlStatistics {
  bowl_type: number;
  count: number;
}

interface GraphData {
  labels: string[];
  datasets: {
    label: string;
    data: number[];
    backgroundColor: string[];
  }[];
}

export function useStatistics() {
  const [statistics, setStatistics] = useState<BowlStatistics[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchStatistics();
  }, []);

  const fetchStatistics = async () => {
    try {
      setLoading(true);
      const { data, error } = await supabase
        .from('statistics')