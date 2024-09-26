import { NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';

// Supabaseクライアントの初期化
const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
);

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const type = searchParams.get('type');

  try {
    switch (type) {
      case 'average':
        return await getAverageAndTrend();
      case 'category':
        const category = searchParams.get('category');
        return await getCategoryStatistics(category);