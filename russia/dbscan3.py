import pandas as pd
import argparse
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import re  # 正規表現モジュール

# コマンドライン引数の解析
def parse_arguments():
    parser = argparse.ArgumentParser(description="CSVファイルからDBSCANでクラスタリングを実行する")
    parser.add_argument('filename', type=str, help='CSVファイルのパス')
    parser.add_argument('--eps', type=float, default=9, help='DBSCANのepsパラメータ')
    parser.add_argument('--min_samples', type=int, default=3, help='DBSCANのmin_samplesパラメータ')
    return parser.parse_args()

# ファイル名から8桁の日付を推測し、YYYY-MM-DD形式に変換
def extract_date_from_filename(filename):
    match = re.search(r'(\d{8})', filename)  # 8桁の数字を抽出
    if match:
        date_str = match.group(1)
        # YYYYMMDD形式からYYYY-MM-DD形式に変換
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
    else:
        return "日付不明"

# メイン処理
if __name__ == "__main__":
    args = parse_arguments()

    # ファイル名から日付を取得
    extracted_date = extract_date_from_filename(args.filename)

    # CSVファイルの読み込み
    try:
        df = pd.read_csv(args.filename)
        #print("データの概要:")
        #print(df.head())

        # 'duration'と'eventcount'列のデータを抽出
        data = df[['duration', 'eventcount']]

        # DBSCANによるクラスタリング
        dbscan = DBSCAN(eps=args.eps, min_samples=args.min_samples)
        clusters = dbscan.fit_predict(data)

        # 結果をDataFrameに追加
        df['cluster'] = clusters

        # クラスタ数とノイズ数の計算
        n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
        n_noise = list(clusters).count(-1)

        # 結果を表示 (日付, クラスタ数, ノイズ数)
        print(f"{extracted_date}, {n_clusters}, {n_noise}")

        # クラスタリングの結果を可視化
        plt.figure(figsize=(8, 6))
        plt.scatter(df['duration'], df['eventcount'], c=df['cluster'], cmap='plasma', marker='o')
        plt.title('DBSCAN Clustering of duration vs. eventcount')
        plt.xlabel('Duration')
        plt.ylabel('Eventcount')
        plt.colorbar(label='Cluster')
        #plt.show()

    except FileNotFoundError:
        print(f"エラー: ファイル '{args.filename}' が見つかりません")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")
