# aws_iot_tweet
AWS の IoT 1-Click で呼び出す Lambda から Twitter につぶやく

# 環境に合わせて修正する箇所
apex/functions/tweet/function.json  
1. "role": "arn:aws:iam::123456789012:role/lambda-execution-role",  
→「123456789012」：自分のAWSアカウントに変更。  
→「lambda-execution-role」：お好きなロールに変更。とりあえずCloudWatch Logsに読み書き可能であればOK  
2. 次のTwitterのAPIキーを設定する  
"ConsumerKey": "enter your Consumer Key",  
"ConsumerSecret": "enter your Consumer Secret",  
"AccessToken": "enter your Access Token",  
"AccesssTokenSecert": "enter your Accesss Token Secert",  
3. つぶやく内容の編集  
"clickType_single": シングルクリック時につぶやく内容  
"clickType_double": ダブルクリック時につぶやく内容  
"clickType_long": ロングクリック時につぶやく内容  


# Lambda関数のデプロイ方法
apexを使っているので、apexディレクトリの下で以下のコマンドを実行。  

```
apex deploy
```

デプロイすると、iot_twitter_tweetというLambda関数が作成される。  
apexを使いたくない場合は、tweetディレクトリ以下をzipで固めて直接Lambdaにアップロードする。  
Lambdaの設定内容はfunction.jsonを参照。  

