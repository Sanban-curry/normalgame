import os
import logging
import argparse
from tqdm import tqdm
import concurrent.futures
import importlib
import threading
import shutil
import time
import traceback
import asyncio
import logging.handlers

# スレッディングモジュールをインポート
# これにより、非同期処理が可能になり、ログ出力を別スレッドで行うことができます

from config.settings import BABEL_GENERATED_DIR


from utils.utils import generate_response, normal

def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.handlers.RotatingFileHandler(
        'domain_exe.log', maxBytes=10*1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logging()

def import_modules(template_saas, system_name):
    logger.info(f"モジュールのインポートを開始: template_saas={template_saas}, system_name={system_name}")
    concept = importlib.import_module(f"{template_saas}.def_concept").concept
    dir_frontend = importlib.import_module(f"{template_saas}.def_concept").dir_structure
    files = importlib.import_module(f"{template_saas}.def_domain").files
    constraints = importlib.import_module(f"{template_saas}.def_constraints").constraints


    root_dir = os.path.expanduser(f"{BABEL_GENERATED_DIR}/{system_name}/temp")
    # root_dir = os.path.expanduser(f"/tmp/babel_generated/{system_name}/{{next-app-name}}/temp")
    logger.debug(f"ルートディレクトリ: {root_dir}")
    logger.info("モジュールのインポートが完了しました")
    return concept, dir_frontend, files, root_dir, constraints

async def create_file(directory, filename, prompt, file_number, concept, dir_frontend, constraints, root_dir, progress_bar, total_files, max_tokens, temperature):
    logger.info(f"ファイル作成開始: {filename}")
    file_path = os.path.join(root_dir, directory)
    os.makedirs(file_path, exist_ok=True)
    file_path = os.path.join(file_path, filename)
    logger.debug(f"ファルパス: {file_path}")
    
    with open(file_path, "w", encoding="utf-8") as f:
        model = "claude-3-5-sonnet-20240620"
        full_prompt = f'''
        {concept}\n{dir_frontend}\n{constraints}\n上記の内容をもとにして{prompt}
        '''
        logger.debug("AIモデルによる応答生成を開始")
        response = generate_response(model, full_prompt, max_tokens, temperature)
        formatted_response = normal(response)
        f.write(formatted_response)
    
    progress_bar.update(1)
    logger.info(f"{file_number}枚目/{total_files}が完了しました。")

    await asyncio.sleep(0)  # 他のタスクに実行を譲る

async def main(template_saas, system_name, next_app_name, max_tokens, temperature):

    # ANTHROPIC_API_KEYの確認と設定
    print("ANTHROPIC_API_KEYの確認を開始します")
    if "ANTHROPIC_API_KEY" not in os.environ:
        print("警告: ANTHROPIC_API_KEYが環境変数に設定されていません")
        api_key = input("ANTHROPIC_API_KEYを入力してください (https://console.anthropic.com/settings/keys): ")
        os.environ["ANTHROPIC_API_KEY"] = api_key
        print(f"ANTHROPIC_API_KEYを環境変数に設定しました: {api_key[:5]}...")
    else:
        print(f"ANTHROPIC_API_KEYが環境変数に設定されています: {os.environ['ANTHROPIC_API_KEY'][:5]}...")

    # # Next.jsアプリケーションの作成
    # # npxをグローバルにインストール
    # print("npxのグローバルインストールを開始します")
    # try:
    #     subprocess.run(["npm", "install", "-g", "npx"], check=True, capture_output=True, text=True)
    #     print("npxのグローバルインストールが完了しました")
    # except subprocess.CalledProcessError as e:
    #     print(f"エラー: npxのインストール中にエラーが発生しました: {e}")
    #     print(f"エラー出力: {e.stderr}")
    #     raise



    # print(f"Next.jsアプリケーション '{next_app_name}' の作成���開始します")


    # create_next_app_command = [
    #     "echo", "y", "|",
    #     "npx", 
    #     "create-next-app@latest", 
    #     next_app_name,
    #     "--typescript",
    #     "--eslint",
    #     "--tailwind",
    #     "--app",
    #     "--no-src-dir",
    #     "--import-alias=\"@/*\""
    # ]
    # print(f"実行するコマンド: {' '.join(create_next_app_command)}")
    # try:
    #     import subprocess
    #     result = subprocess.run(create_next_app_command, check=True, capture_output=True, text=True)
    #     print(f"Next.jsアプリケーションの作成が完了しました。出力:")
    #     print(result.stdout)
    # except subprocess.CalledProcessError as e:
    #     print(f"エラー: Next.jsアプリケーションの作成中にエラーが発生しました: {e}")
    #     print(f"エラー出力: {e.stderr}")
    #     raise

    print(f"メイン処理開始: template_saas={template_saas}, system_name={system_name}, next_app_name={next_app_name}")
    concept, dir_frontend, files, root_dir, constraints = import_modules(template_saas, system_name)
    print(f"インポートされたモジュール情報: concept={concept[:50]}..., dir_frontend={dir_frontend[:50]}..., files数={len(files)}, root_dir={root_dir}, constraints={constraints[:50]}...")
    
    root_dir = root_dir.replace("{next-app-name}", next_app_name)
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
        print(f"ルートディレクトリを作成しました: {root_dir}")
    else:
        print(f"ルートディレクトリが既に存在します: {root_dir}")

    progress_bar = tqdm(total=len(files), unit="files")
    print(f"合計ファイル数: {len(files)}")

    tasks = [create_file(directory, filename, prompt, i+1, concept, dir_frontend, constraints, root_dir, progress_bar, len(files), max_tokens, temperature) 
             for i, (directory, filename, prompt) in enumerate(files)]
    await asyncio.gather(*tasks)

    progress_bar.close()
    print("すべてのファイル生成が完了しました")

    # # .env.localファイルをnext_app_nameディレクトリにコピーする
    # print(f".env.localファイルを{next_app_name}ディレクトリにコピーします")
    # try:
    #     shutil.copy('.env.local', os.path.join(next_app_name, '.env.local'))
    #     print(f".env.localファイルのコピーが完了しました: {os.path.join(next_app_name, '.env.local')}")
    # except FileNotFoundError:
    #     print(f"エラー: .env.localファイルが見つかりません")
    # except PermissionError:
    #     print(f"エラー: .env.localファイルのコピー中に権限エラーが発生しました")
    # except Exception as e:
    #     print(f"エラー: .env.localファイルのコピー中に予期せぬエラーが発生しました: {e}")

    # # Next.jsアプリケーションのディレクトリに移動
    # print(f"{next_app_name}ディレクトリに移動します")
    # os.chdir(next_app_name)
    # print(f"現在のディレクトリ: {os.getcwd()}")

    # # 追加のパッケージをインストール
    # print("追加のパッケージをインストールします")
    # 追加パッケージ = [
    #     "react-hook-form@^7.x.x",
    #     "@supabase/supabase-js@^2.x.x",
    #     "@supabase/auth-helpers-nextjs@^0.x.x",
    #     "lucide-react@^0.x.x",
    #     "bufferutil@^4.x.x",
    #     "utf-8-validate@^5.x.x",
    #     "react-chartjs-2@^5.x.x"  # react-chartjs-2を追加
    # ]
    
    # for パッケージ in 追加パッケージ:
    #     try:
    #         print(f"{パッケージ} のインストールを開始します")
    #         result = subprocess.run(["npm", "install", パッケージ], check=True, capture_output=True, text=True)
    #         print(f"{パッケージ} のインストールが完了しました。出力:")
    #         print(result.stdout)
    #     except subprocess.CalledProcessError as e:
    #         print(f"エラー: {パッケージ} のインストール中にエラーが発生しました: {e}")
    #         print(f"エラー出力: {e.stderr}")
    #         raise
    
    # print("すべての追加パッケージのインストールが完了しました")

    
    # 依存関係のインストール
    # print("npm installを実行します")
    # try:
    #     result = subprocess.run(["npm", "install"], check=True, capture_output=True, text=True)
    #     print("npm installが正常に完了し���した。出力:")
    #     print(result.stdout)
    # except subprocess.CalledProcessError as e:
    #     print(f"エラ: npm installの実行中にエラーが発生しました: {e}")
    #     print(f"エラー出力: {e.stderr}")
    #     raise

    # # 開発サーバーの起動
    # print("npm run devを実行します")
    # try:
    #     # サブプロセスとして開発サーバーを起動
    #     dev_process = subprocess.Popen(["npm", "run", "dev"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #     print("開発サーバーが起動しました")
        
    #     # ログ出力を非同期で処理
    #     def log_output(stream, log_func):
    #         for line in stream:
    #             log_func(f"開発サーバー出力: {line.strip()}")
        
    #     threading.Thread(target=log_output, args=(dev_process.stdout, print)).start()
    #     threading.Thread(target=log_output, args=(dev_process.stderr, print)).start()
        
    #     # メインプロセスを継続させるために一定時間待機
    #     print("開発サーバーの起動を待機中...")
    #     time.sleep(10)  # 10秒間待機（必要に応じて調整）
        
    #     print("開発サーバーが正常に動作しています")
    # except Exception as e:
    #     print(f"エラー: 開発サーバ���の起動中にエラーが発生しました: {e}")
    #     raise

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="SaaSアプリケーション生成スクリプト")
        parser.add_argument("-t", "--template_saas", required=True, help="テンプレートSaaS名を指定してください")
        parser.add_argument("-s", "--system_name", required=True, help="システム名を指定してください")
        parser.add_argument("-na", "--next_app_name", required=True, help="Next.jsアプリケーション名を指定してください")
        parser.add_argument("-mt", "--max_tokens", type=int, default=300, help="生成する最大トークン数")
        parser.add_argument("-temp", "--temperature", type=float, default=0.5, help="生成の温度パラメータ")
        args = parser.parse_args()
        
        logger.info("スクリプト実行開始")
        asyncio.run(main(args.template_saas, args.system_name, args.next_app_name, args.max_tokens, args.temperature))
        logger.info("スクリプト実行終了")
    except Exception as e:
        logger.error(f"スクリプト実行中にエラーが発生しました: {str(e)}")
        logger.error(traceback.format_exc())
        sys.exit(1)