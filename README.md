# DHT11 Pythonをベースにした温湿度送信ツール
 DHT11 Pythonをベースにした温湿度送信ツールです。  
 宛先URLにPOSTさせます。  

---

## 環境変数について
- PIN  
センサーが接続されているGPIOピンの番号を指定します
- POST_ADDR  
送信先のURLを指定します。送信先へはPostメソッドでjson形式で送信されます。
    ```json
    
    ```
- INTERVAL  
送信間隔を秒単位で指定します。
  
---
## Setting(docker&plain)
- app/.env
```sh
PIN=14 # your GPIO PIN
POST_ADDR=http://127.0.0.1/temp # POST Server URL
INTERVAL=300 # send interval(second)
```

## Setting(Kubernetes)
- manifests.yaml
```yaml
~~~
env:
    - name: PIN
      value: "14" # your GPIO PIN
    - name: POST_ADDR
      value: "http://127.0.0.1/temp" # POST Server URL
    - name: INTERVAL
      value: "300" # send interval(second)
~~~
```