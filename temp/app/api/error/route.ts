// app/api/error/route.ts

import { NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';
import nodemailer from 'nodemailer';

// Supabaseクライアントの初期化
const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
);

// エラーログをデータベースに記録する関数
async function logError(error: any) {
  const { data, error: dbError } = await supabase
    .from('error_logs')
    .insert({
      message: error.message,
      stack: error.stack,
      timestamp: new Date().toISOString(),
    });

  if (dbError) {