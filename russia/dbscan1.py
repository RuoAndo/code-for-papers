import pandas as pd
import argparse
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# コマンドライン引数の解析
def parse_arguments():
    parser = argparse.ArgumentParser(description="CSVファイルからDBSCANでクラスタリングを実行する")
    parser.add_argument('filename', type=str, help='CSVファイルのパス')
    parser.add_argument('--eps', type=float, default=5.0, help='DBSCANのepsパラメータ')
    parser.add_argument('--min_samples', type=int, default=3, help='DBSCANのmin_samplesパラメータ')
    return parser.parse_args()

# メイン処理
if __name__ == "__main__":
    args = parse_arguments()

    # CSVファイルの読み込み
    try:
        df = pd.read_csv(args.filename)
        print("データの概要:")
        print(df.head())

        # 'duration'と'eventcount'列のデータを抽出
        data = df[['duration', 'eventcount']]

        # DBSCANによるクラスタリング
        dbscan = DBSCAN(eps=args.eps, min_samples=args.min_samples)
        clusters = dbscan.fit_predict(data)

        # 結果をDataFrameに追加
        df['cluster'] = clusters

        print("\nクラスタリング結果:")
        print(df[['duration', 'eventcount', 'cluster']])

        # クラスタリングの結果を可視化
        plt.figure(figsize=(8, 6))
        plt.scatter(df['duration'], df['eventcount'], c=df['cluster'], cmap='plasma', marker='o')
        plt.title('DBSCAN Clustering of duration vs. eventcount')
        plt.xlabel('Duration')
        plt.ylabel('Eventcount')
        plt.colorbar(label='Cluster')
        plt.show()

    except FileNotFoundError:
        print(f"エラー: ファイル '{args.filename}' が見つかりません")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")
