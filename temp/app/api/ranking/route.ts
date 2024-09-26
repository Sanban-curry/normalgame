import { NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';

// Supabaseクライアントの初期化
const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_ANON_KEY!);

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const limit = searchParams.get('limit') ? parseInt(searchParams.get('limit')!) : 100;
  const offset = searchParams.get('offset') ? parseInt(searchParams.get('offset')!) : 0;

  try {
    const { data, error } = await supabase
      .from('users')
      .select('id, username, score')
      .order('score', { ascending: false })
      .range(offset