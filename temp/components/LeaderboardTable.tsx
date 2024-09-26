import { useState } from 'react';
import { createServerComponentClient } from '@supabase/auth-helpers-nextjs';
import { cookies } from 'next/headers';
import type { Database } from '@/types/supabase';

type Player = {
  id: string;
  username: string;
  score: number;
  playCount: number;
};

type SortField = 'score' | 'playCount';

async function LeaderboardTable({
  page = 1,
  pageSize = 10,
  sortBy = 'score' as SortField,
  sortOrder = 'desc' as 'asc' | 'desc'
}) {
  const supabase = createServerComponentClient<Database>({ cookies });

  // データベースからプレイヤーデータを取得
  const { data: players, error } = await supabase