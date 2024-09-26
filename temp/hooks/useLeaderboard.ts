'use client';

import { useState, useEffect } from 'react';
import { supabase } from '../lib/supabase';

interface LeaderboardEntry {
  id: string;
  username: string;
  score: number;
  rank: number;
}

type SortOrder = 'asc' | 'desc';

export function useLeaderboard() {
  const [leaderboard, setLeaderboard] = useState<LeaderboardEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [sortOrder, setSortOrder] = useState<SortOrder>('desc');
  const [filter, setFilter] = useState('');

  useEffect(() => {
    fetchLeaderboard();
  }, []);

  const fetchLeaderboard = async () => {
    try {
      setLoading(