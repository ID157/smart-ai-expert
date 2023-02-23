# Overview
LangChainを使用して、ChatGPTにドメイン知識をもぐもぐさせます。

# Setup
1. OpenAI の key を入手する。
参考：https://github.com/openai/openai-python

2. 入手した key を使用して .env ファイルを作成する

```.env
OPENAI_API_KEY='<1で入手したKEY>'
```

# Usage
1. 学習させたいデータを、data/ 以下に data/<そのデータの名前>/data.txt という形式で保存します。
2. `$ python main.py init data` を実行し、良い感じに`index.json`が作成されることを確認します。
3. `$python main.py add <学習させたいデータの名前>`で、データを学習させます。（`index.json` が更新されていそうなら成功です。）
4. `python main.py query "質問です！　PはNPでしょうか"`のような形式で、ChatGPTに質問できます。

