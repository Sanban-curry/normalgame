# システム生成NormaBowlゲームプラットフォームの定義

import os
from nextjs.def_concept import concept, dir_structure
from nextjs.def_constraints import page_tsx

# プロジェクトNormaBowlの詳細定義
def_domain = concept + dir_structure

# 作成するファイルの定義
files = [
    ('app', 'page.tsx',
     def_domain + page_tsx + """
     page.tsxファイルにNormaBowlゲームのメインページを実装してください。
     - ゲームの説明と開始ボタン
     - 最新の統計情報の概要表示
     - ランキングやリーダーボードへのリンク
     サーバーコンポーネントとして実装し、React hooksは使用しないでください。
     Header.tsxとFooter.tsx以外のコンポーネントは呼び出さないでください。
     """
    ),
    ('app/game', 'page.tsx',
     def_domain + page_tsx + """
     game/page.tsxファイルにゲームプレイ画面を実装してください。
     - お茶碗の盛り型選択インターフェース
     - プレイヤーの選択と統計データの比較表示
     - フィードバックとスコア表示
     ハイブリッドコンポーネントとして実装し、必要に応じてクライアントサイドの機能を使用してください。
     Header.tsx、Footer.tsx、BowlSelector.tsx、ComparisonDisplay.tsx以外のコンポーネントは呼び出さないでください。
     """
    ),
    ('app/stats', 'page.tsx',
     def_domain + page_tsx + """
     stats/page.tsxファイルに統計情報表示ページを実装してください。
     - 全体の統計データ表示
     - グラフや図表を用いた視覚化
     - フィルタリングオプション
     サーバーコンポーネントとして実装し、React hooksは使用しないでください。
     Header.tsx、Footer.tsx、StatsDisplay.tsx以外のコンポーネントは呼び出さないでください。
     """
    ),
    ('app/ranking', 'page.tsx',
     def_domain + page_tsx + """
     ranking/page.tsxファイルにランキングページを実装してください。
     - プレイヤーのランキング表示
     - スコアや達成バッジの表示
     - フィルタリングと並べ替えオプション
     サーバーコンポーネントとして実装し、React hooksは使用しないでください。
     Header.tsx、Footer.tsx、RankingList.tsx以外のコンポーネントは呼び出さないでください。
     """
    ),
    ('app/profile', 'page.tsx',
     def_domain + page_tsx + """
     profile/page.tsxファイルにユーザープロフィールページを実装してください。
     - ユーザーの個人統計
     - 獲得バッジやアチーブメント
     - プレイ履歴
     サーバーコンポーネントとして実装し、React hooksは使用しないでください。
     Header.tsx、Footer.tsx、ProfileDisplay.tsx以外のコンポーネントは呼び出さないでください。
     """
    ),
    ('components', 'Header.tsx',
     def_domain + """
     Header.tsxファイルにヘッダーコンポーネントを実装してください。
     クライアントコンポーネントのため、ファイルの先頭に'use client';を追加してください。
     - ロゴ
     - ナビゲーションメニュー
     - ユーザーアカウント情報/ログインボタン
     外部コンポーネントは呼び出さないでください。
     """
    ),
    ('components', 'Footer.tsx',
     def_domain + """
     Footer.tsxファイルにフッターコンポーネントを実装してください。
     - コピーライト情報
     - プライバシーポリシーへのリンク
     - お問い合わせフォームへのリンク
     サーバーコンポーネントとして実装し、React hooksは使用しないでください。
     外部コンポーネントは呼び出さないでください。
     """
    ),
    ('components', 'BowlSelector.tsx',
     def_domain + """
     BowlSelector.tsxファイルにお茶碗の盛り型選択コンポーネントを実装してください。
     クライアントコンポーネントのため、ファイルの先頭に'use client';を追加してください。
     - 複数の盛り型オプションの表示
     - インタラクティブな選択機能
     - 選択結果の親コンポーネントへの通知
     外部コンポーネントは呼び出さないでください。
     """
    ),
    ('components', 'ComparisonDisplay.tsx',
     def_domain + """
     ComparisonDisplay.tsxファイルに比較結果表示コンポーネントを実装してください。
     - プレイヤーの選択と統計データの視覚的比較
     - ズレの大きさに応じたフィードバック表示
     - アニメーションやトランジション効果
     サーバーコンポーネントとして実装し、React hooksは使用しないでください。
     外部コンポーネントは呼び出さないでください。
     """
    ),
    ('components', 'StatsDisplay.tsx',
     def_domain + """
     StatsDisplay.tsxファイルに統計情報表示コンポーネントを実装してください。
     - グラフや図表を用いた統計データの視覚化
     - データフィルタリングオプション
     - ツールチップによる詳細情報表示
     クライアントコンポーネントのため、ファイルの先頭に'use client';を追加してください。
     外部コンポーネントは呼び出さないでください。
     """
    ),
    ('components', 'RankingList.tsx',
     def_domain + """
     RankingList.tsxファイルにランキングリスト表示コンポーネントを実装してください。
     - プレイヤーのランキング表示
     - スコアや達成バッジの表示
     - ページネーションまたは無限スクロール機能
     サーバーコンポーネントとして実装し、React hooksは使用しないでください。
     外部コンポーネントは呼び出さないでください。
     """
    ),
    ('components', 'ProfileDisplay.tsx',
     def_domain + """
     ProfileDisplay.tsxファイルにユーザープロフィール表示コンポーネントを実装してください。
     - ユーザーの個人統計表示
     - 獲得バッジやアチーブメントの表示
     - プレイ履歴のタイムライン表示
     サーバーコンポーネントとして実装し、React hooksは使用しないでください。
     外部コンポーネントは呼び出さないでください。
     """
    ),
    ('lib', 'supabase.ts',
     def_domain + """
     supabase.tsファイルにSupabaseクライアントの初期化と設定を記載してください。
     - Supabaseの接続情報の設定
     - 認証関連の関数の実装
     - データ取得・更新関数の実装
     """
    ),
    ('utils', 'gameLogic.ts',
     def_domain + """
     gameLogic.tsファイルにゲームロジック関連の関数を実装してください。
     - プレイヤーの選択と統計データの比較ロジック
     - スコア計算アルゴリズム
     - フィードバック生成ロジック
     """
    ),
    ('utils', 'statsCalculator.ts',
     def_domain + """
     statsCalculator.tsファイルに統計計算用のユーティリティ関数を実装してください。
     - 平均値、中央値、標準偏差の計算
     - パーセンタイルの計算
     - データの正規化と標準化
     """
    ),
    ('app/api/game', 'route.ts',
     def_domain + """
     game/route.tsファイルにゲームプレイ関連のAPIエンドポイントを実装してください。
     - プレイヤーの選択の保存
     - 比較結果の取得
     - スコアの計算と保存
     """
    ),
    ('app/api/stats', 'route.ts',
     def_domain + """
     stats/route.tsファイルに統計データ管理用のAPIエンドポイントを実装してください。
     - 全体統計データの取得
     - 新しいデータの追加と平均値の更新
     - フィルタリングされた統計データの取得
     """
    ),
    ('app/api/ranking', 'route.ts',
     def_domain + """
     ranking/route.tsファイルにランキング管理用のAPIエンドポイントを実装してください。
     - ランキングデータの取得
     - スコアの更新とランキングの再計算
     - フィルタリングされたランキングデータの取得
     """
    ),
    ('app/api/profile', 'route.ts',
     def_domain + """
     profile/route.tsファイルにユーザープロフィール管理用のAPIエンドポイントを実装してください。
     - ユーザープロフィールデータの取得
     - プロフィール情報の更新
     - プレイ履歴の取得と更新
     """
    ),
    ('hooks', 'useGame.ts',
     def_domain + """
     useGame.tsファイルにゲームプレイ管理用のカスタムフックを実装してください。
     クライアントサイド専用のため、ファイルの先頭に'use client';を追加してください。
     - プレイヤーの選択の管理
     - 比較結果の取得と状態管理
     - スコアの計算と保存
     """
    ),
    ('hooks', 'useStats.ts',
     def_domain + """
     useStats.tsファイルに統計データ管理用のカスタムフックを実装してください。
     クライアントサイド専用のため、ファイルの先頭に'use client';を追加してください。
     - 統計データの取得と状態管理
     - データのフィルタリングと更新
     - グラフデータの生成
     """
    ),
    ('hooks', 'useRanking.ts',
     def_domain + """
     useRanking.tsファイルにランキング管理用のカスタムフックを実装してください。
     クライアントサイド専用のため、ファイルの先頭に'use client';を追加してください。
     - ランキングデータの取得と状態管理
     - ランキングのフィルタリングと並べ替え
     - ユーザーのランク変動の追跡
     """
    ),
    ('hooks', 'useProfile.ts',
     def_domain + """
     useProfile.tsファイルにユーザープロフィール管理用のカスタムフックを実装してください。
     クライアントサイド専用のため、ファイルの先頭に'use client';を追加してください。
     - プロフィールデータの取得と状態管理
     - プロフィール情報の更新
     - プレイ履歴の取得と管理
     """
    ),
    ('types', 'index.ts',
     def_domain + """
     index.tsファイルにTypeScript型定義を実装してください。
     - ゲームデータ、統計データ、ランキング、プロフィールなどの型定義
     - APIレスポンスの型定義
     - ユーティリティ型の定義
     """
    ),
    ('scripts', 'setup_supabase.sh',
     def_domain + """
     setup_supabase.shファイルにSupabaseの設定と構築を行うシェルスクリプトを実装してください。
     - Supabaseプロジェクトの作成
     - データベーステーブルの作成（ゲームデータ、統計、ランキング、ユーザープロフィールなど）
     - 初期データの挿入
     - 認証設定の構成
     - RLSポリシーの設定
     - 環境変数の設定（.env.localファイルの作成）
     """
    ),
    ('app/api/error', 'route.ts',
     def_domain + """
     error/route.tsファイルにエラー処理用のAPIルートを実装してください。
     - エラーログの記録
     - エラー通知の送信（オプション）
     - クライアントへのエラーレスポンスの返却
     """
    ),
    ('components', 'ErrorBoundary.tsx',
     def_domain + """
     ErrorBoundary.tsxファイルにReactエラーバウンダリコンポーネントを実装してください。
     - エラーのキャッチと表示
     - エラー情報の収集
     - エラーリカバリーオプションの提供
     クライアントコンポーネントとして実装し、use clientディレクティブを使用してください。
     """
    ),
    ('utils', 'errorLogger.ts',
     def_domain + """
     errorLogger.tsファイルにエラーロギング用のユーティリティ関数を実装してください。
     - エラー情報の構造化
     - ログの保存（ファイルまたはデータベース）
     - 重要度に応じたログレベルの設定
     """
    ),
    ('hooks', 'useErrorHandler.ts',
     def_domain + """
     useErrorHandler.tsカスタムフックを実装してください。
     - エラー状態の管理
     - エラーメッセージの表示制御
     - エラー報告機能の提供
     クライアントコンポーネント用のフックとして実装してください。
     """
    ),
]

# package.jsonに追加する依存関係
package_json_dependencies = """
    "react-hook-form": "^7.x.x",
    "@supabase/supabase-js": "^2.x.x",
    "@supabase/auth-helpers-nextjs": "^0.x.x",
    "lucide-react": "^0.x.x",
    "recharts": "^2.x.x",
    "d3": "^7.x.x",
    "framer-motion": "^10.x.x",
    "i18next": "^23.x.x",
    "react-i18next": "^13.x.x",
    "zod": "^3.x.x",
    "bufferutil": "^4.x.x",
    "utf-8-validate": "^5.x.x"
"""

# package.jsonファイルの定義を追加
files.append(('', 'package.json', 
    def_domain + f"""
    package.jsonファイルに必要な依存関係を追加してください。
    以下の依存関係を"dependencies"セクションに追加してください：
    {package_json_dependencies}
    """
))