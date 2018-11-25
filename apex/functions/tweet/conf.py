# -*- coding: utf-8 -*-

import os

ConsumerKey = os.environ['ConsumerKey'] # * enter your Consumer Key *
ConsumerSecret = os.environ['ConsumerSecret']   # * enter your Consumer Secret *
AccessToken = os.environ['AccessToken'] # * enter your Access Token *
AccesssTokenSecert = os.environ['AccesssTokenSecert']   # * enter your Accesss Token Secert *
clickType_single = os.environ['clickType_single']   # * 改行を入れたい場合は、\\nを環境変数に入れ、.replace('\\n', '\n')で変換する
clickType_double = os.environ['clickType_double']
clickType_long = os.environ['clickType_long']

UPDATE_URL = 'https://api.twitter.com/1.1/statuses/update.json'
