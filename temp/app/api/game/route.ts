import { NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';

// Supabaseクライアントの初期化
const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
);

export async function POST(request: Request) {
  try {
    const { userId, bowlType } = await request.json();

    // プレイヤーの選択を保存
    const { data: selectionData, error: selectionError } = await supabase
      .from('bowl_selections')
      .insert({ user_id: userId, bowl_type: bowlType })
      .select();

    if (selectionError) throw selectionError;

    // 統計データを取得
    const { data: statsData, errorse