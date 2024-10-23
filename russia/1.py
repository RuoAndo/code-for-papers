import pandas as pd
import argparse

# コマンドライン引数を解析する関数
def parse_arguments():
    parser = argparse.ArgumentParser(description="CSVファイルを読み込んでDataFrameに変換する")
    parser.add_argument('filename', type=str, help='読み込むCSVファイルのパス')
    return parser.parse_args()

# メイン処理
if __name__ == "__main__":
    args = parse_arguments()
    filename = args.filename  # 引数からファイル名を取得

    # DataFrameにCSVを読み込む
    try:
        df = pd.read_csv(filename)
        print(df)
    except FileNotFoundError:
        print(f"エラー: ファイル '{filename}' が見つかりません")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")
