'use client';

import { useState, useEffect } from 'react';
import { supabase } from '@/lib/supabase';

type RankingEntry = {
  id: string;
  username: string;
  score: number;
  rank: number;
  previousRank: number;
};

type SortOrder = 'asc' | 'desc';

export default function useRanking() {
  const [rankings, setRankings] = useState<RankingEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [sortOrder, setSortOrder] = useState<SortOrder>('desc');
  const [filter, setFilter] = useState<string>('');

  useEffect(() => {
    fetchRankings();
  }, []);