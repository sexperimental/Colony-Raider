import requests
import random
import string
import time 

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

url = "https://minecraft-mcworld.com/wp-comments-post.php"

id = input("URLにある数字を入力してください: ")
comment = input("コメントしたい文字を入力してください: ")
count = int(input("何個のコメントを送信しますか: "))

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

try:
    session = requests.Session()
    
    for i in range(count):
        data = {
            "comment": comment + "_" + randomword(5) + f"   私のMCIDはWater6528です。",
            "comment_post_ID": id,
        }

        sleep_time = random.uniform(15, 15)
        time.sleep(sleep_time)

        try:
            response = session.post(url, headers=headers, data=data, timeout=10)
            response.raise_for_status()
            print(f"コメント {i+1}/{count} が送信されました。")
        except requests.exceptions.RequestException as e:
            print(f"コメント {i+1} の送信でエラーが発生しました: {e}")
            continue

    print(f"完了。")
    
except requests.exceptions.Timeout:
    print("リクエストがタイムアウトしました。")
except requests.exceptions.RequestException as e:
    print(f"リクエスト中にエラーが発生しました: {e}")
