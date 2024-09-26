// utils/errorLogger.ts

import { createClient } from '@supabase/supabase-js';

// Supabaseクライアントの初期化
const supabase = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);

// ログレベルの定義
enum LogLevel {
  INFO = 'INFO',
  WARNING = 'WARNING',
  ERROR = 'ERROR',
  CRITICAL = 'CRITICAL',
}

// エラーログの構造
interface ErrorLog {
  timestamp: string;
  level: LogLevel;
  message: string;
  stack?: string;
  userId?: string;
  additionalInfo?: Record<string, unknown>;
}

// エラーログをデータベースに保存する関数
async function saveLog