concept = """
# NormaBowl - お茶碗の盛り型で「普通」を再発見するゲーム

## 1. プロジェクトコンセプト

NormaBowlは、プレイヤーの「普通」の基準を社会的な平均と比較し、そのズレを視覚的に表示する革新的なゲームプラットフォームです。お茶碗の盛り型を題材に、ユーザーが自身の「普通」を再確認し、社会的な平均との違いを楽しみながら理解できる環境を提供します。

主要機能：
1. ユーザー入力：プレイヤーの「普通」の選択
2. 統計データ参照：蓄積されたデータからの平均値計算
3. 比較表示：ユーザー選択と統計平均の視覚的比較
4. フィードバック：ズレに基づくコメント提供
5. データ蓄積：新規データの統計への追加
6. ゲーム要素：ランキングや達成システム
7. 多言語対応：グローバルなユーザー獲得

## 2. システム概要

NormaBowlは、Next.js 13のApp Routerを使用して以下の主要コンポーネントで構成されます：

1. ユーザー入力インターフェース
2. 統計データ処理エンジン
3. 比較・可視化モジュール
4. フィードバック生成システム
5. データベース管理システム
6. ゲーミフィケーション機能
7. 多言語サポートモジュール

## 3. 技術スタック

- フロントエンド：Next.js 13 (React) with App Router
- スタイリング：Tailwind CSS
- バックエンド：Next.js API Routes
- データベース：Supabase (PostgreSQL)
- 認証：Supabase Auth
- デプロイ：Vercel
- 国際化：next-i18next
- グラフ描画：D3.js または Chart.js

## 4. セキュリティ要件

- HTTPS通信の強制
- ユーザーデータの匿名化
- アクセス制御と権限管理
- セキュリティ監査ログ
- 定期的なバックアップ

## 5. スケーラビリティと性能

- サーバーレスアーキテクチャの採用（Vercel + Supabase）
- キャッシュ戦略の最適化（Next.js の ISR を活用）
- エッジコンピューティングの利用（Vercel Edge Functions）

## 6. データベース定義

NormaBowlのデータベースは、Supabase（PostgreSQL）を使用して以下のテーブルで構成されます：

1. users（ユーザー）テーブル
   - id: UUID (主キー)
   - username: TEXT (ユーザー名)
   - email: TEXT (メールアドレス)
   - created_at: TIMESTAMP (作成日時)
   - last_login: TIMESTAMP (最終ログイン日時)

2. bowl_selections（お茶碗選択）テーブル
   - id: UUID (主キー)
   - user_id: UUID (外部キー、usersテーブルを参照)
   - bowl_type: INTEGER (選択されたお茶碗の盛り型)
   - created_at: TIMESTAMP (選択日時)

3. statistics（統計）テーブル
   - id: UUID (主キー)
   - bowl_type: INTEGER (お茶碗の盛り型)
   - count: INTEGER (選択された回数)
   - updated_at: TIMESTAMP (最終更新日時)

4. feedback（フィードバック）テーブル
   - id: UUID (主キー)
   - deviation_range: TEXT (ズレの範囲)
   - message: TEXT (フィードバックメッセージ)
   - language: TEXT (言語コード)

5. achievements（達成）テーブル
   - id: UUID (主キー)
   - user_id: UUID (外部キー、usersテーブルを参照)
   - achievement_type: TEXT (達成の種類)
   - achieved_at: TIMESTAMP (達成日時)

6. language_preferences（言語設定）テーブル
   - id: UUID (主キー)
   - user_id: UUID (外部キー、usersテーブルを参照)
   - language: TEXT (選択言語)
   - updated_at: TIMESTAMP (更新日時)

これらのテーブルは、NormaBowlの運用に必要な全ての情報を効率的に管理し、システムの各機能をサポートします。Supabaseの機能を活用することで、データの整合性を保ちながら、高速なクエリとリアルタイムの更新を実現します。
"""

dir_structure = """
normabowl/
│
├── app/
│   ├── api/
│   │   ├── selections/
│   │   │   └── route.ts
│   │   ├── statistics/
│   │   │   └── route.ts
│   │   ├── feedback/
│   │   │   └── route.ts
│   │   ├── achievements/
│   │   │   └── route.ts
│   │   └── users/
│   │       └── route.ts
│   ├── game/
│   │   └── page.tsx
│   ├── results/
│   │   └── page.tsx
│   ├── leaderboard/
│   │   └── page.tsx
│   ├── profile/
│   │   └── page.tsx
│   ├── layout.tsx
│   └── page.tsx
│
├── components/
│   ├── BowlSelector.tsx
│   ├── ComparisonChart.tsx
│   ├── FeedbackDisplay.tsx
│   ├── AchievementBadge.tsx
│   ├── LanguageSelector.tsx
│   ├── Navbar.tsx
│   └── Footer.tsx
│
├── lib/
│   ├── supabase.ts
│   └── i18n.ts
│
├── utils/
│   ├── statisticsCalculator.ts
│   ├── achievementChecker.ts
│   └── helpers.ts
│
├── hooks/
│   ├── useSelection.ts
│   ├── useStatistics.ts
│   ├── useFeedback.ts
│   └── useAchievements.ts
│
├── types/
│   └── index.ts
│
├── public/
│   ├── images/
│   │   └── bowls/
│   ├── locales/
│   └── favicon.ico
│
├── .env.local
├── next.config.js
├── tsconfig.json
├── package.json
└── vercel.json
"""