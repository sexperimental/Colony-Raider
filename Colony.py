import requests
import random
import string
import time 

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

url = "https://minecraft-mcworld.com/wp-comments-post.php"

id = input("投稿IDを入力してください: ")
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
            "author": "",
            "email": "",
            "url": "",
            "submit": "コメントを送信",
            "comment_post_ID": id,
            "comment_parent": "0",
            "akismet_comment_nonce": "aa3d2604ca",
            "ak_hp_textarea": "",
            "ak_js": "1732444997676",
            "ak_bib": "1732445006725",
            "ak_bfs": "1732445009032",
            "ak_bkpc": "5",
            "ak_bkp": "137;74,771;147,93;91,80;78,63;","ak_bmc": "64;96,4551;85,550;97,139;47,2346;","ak_bmcc": "5",
            "ak_bmk": "",
            "ak_bck": "1;1",
            "ak_bmmc": "5",
            "ak_btmc": "0",
            "ak_bsc": "6",
            "ak_bte": "",
            "ak_btec": "0",
            "ak_bmm": "823,9257;810,476;592,10862;1293,10912;19,11304;",
        }

        sleep_time = random.uniform(15, 17)
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
