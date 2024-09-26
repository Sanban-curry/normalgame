'use client';

import { useState, useEffect } from 'react';
import { supabase } from '@/lib/supabase';

interface BowlStats {
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

export function useStats() {
  const [stats, setStats] = useState<BowlStats[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      setLoading(true);
      const { data, error } = await supabase
        .from('statistics')
        .select('*')
        .order('bowl