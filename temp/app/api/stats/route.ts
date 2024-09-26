import { NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';

// Supabaseクライアントの初期化
const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
);

// 全体統計データの取得
export async function GET() {
  try {
    const { data, error } = await supabase
      .from('statistics')
      .select('*')
      .order('bowl_type', { ascending: true });

    if (error) throw error;

    return NextResponse.json(data);
  } catch (error) {
    console.error('統計データの取得に失