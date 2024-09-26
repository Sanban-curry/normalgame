#!/bin/bash

# Supabaseプロジェクトの作成
echo "Supabaseプロジェクトを作成中..."
PROJECT_ID=$(supabase projects create NormaBowl --org-id your_org_id)
supabase link --project-ref $PROJECT_ID

# データベーステーブルの作成
echo "データベーステーブルを作成中..."
supabase db push

# SQL実行関数
execute_sql() {
    supabase db run "$1"
}

# ユーザーテーブルの作成
execute_sql "
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);
"

# お茶碗選択テーブルの作成
execute_