import { Suspense } from 'react';
import { createServerComponentClient } from '@supabase/auth-helpers-nextjs';
import { cookies } from 'next/headers';
import type { Database } from '@/types/supabase';

type Player = {
  id: string;
  username: string;
  score: number;
  badges: string[];
};

async function fetchRankingData(page: number, pageSize: number): Promise<{ players: Player[], totalCount: number }> {
  const supabase = createServerComponentClient<Database>({ cookies });
  
  const start = (page - 1) * pageSize;
  const end = start + pageSize - 1;

  const { data: players, error, count } = await supabase
    .from('users')
    .select(`
      i