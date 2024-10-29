import requests

def check_ip(ip_address, api_key):
    url = "https://api.abuseipdb.com/api/v2/check"
    querystring = {
        "ipAddress": ip_address,
        "maxAgeInDays": "90"  # 過去90日間のデータを取得
    }
    headers = {
        "Accept": "application/json",
        "Key": api_key
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        print(f"IP: {data['data']['ipAddress']}")
        print(f"信頼度スコア: {data['data']['abuseConfidenceScore']}")
        print("報告履歴:")
        for report in data['data']['reports']:
            print(f"- 日付: {report['reportedAt']}, カテゴリ: {report['categories']}, コメント: {report.get('comment', 'なし')}")
    else:
        print(f"エラー: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # チェックしたいIPアドレスとAPIキーを設定
    ip_address = "123.123.123.123"  # 例: 任意のIP
    api_key = "あなたのAPIキー"

    check_ip(ip_address, api_key)
