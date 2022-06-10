# LSA_II_Shopping

## Concept Development 發展理念

## 安裝 & 設定過程
* 作業系統：Linux
* Linux 安裝 Docker
```terminal=
$ sudo apt-get install -y curl
$ curl -s https://get.docker.com | sudo sh 
```
* 安裝 nginx
* 建立 Dockerfile，內容如下
    * 安裝 Python
    * 安裝 Flask
* 安裝 `selenium`
```bash=
pip install selenium
```
* 測試看看有沒有安裝成功
    * 建立一個 python 檔案
    ```bash=
    import selenium
    ```
    * 執行這個 python 檔
    * 如果可以執行的話代表安裝成功
* 下載跟 Google Chrome 同樣版本的 ChromeDriver
    * 先查看瀏覽器的版本
        * 查看瀏覽器的版本
        * 左上角的三個圓點 => 說明 => 關於 Google Chrome
        * ![](https://i.imgur.com/ZgGJlbt.png)
        * ![](https://i.imgur.com/4dc1LRr.png)
    * 進入此連結下載 ChromeDriver：https://sites.google.com/chromium.org/driver/
    * ![](https://i.imgur.com/34eXpKM.png)


## LSA 課堂知識運用
* 切換到 container
`docker exec -it <containerID> /bin/sh`
* `/usr/local/bin/python -m pip install --upgrade pip`
* <none>:`docker image prune --filter="dangling=true"`

## Job_Assign

| 組員 | 工作分配 |
| -------- | -------- | 
| 林惠霖 | 後端、爬蟲 | 
| 楊心慈 | 前端、docker |

## References
* Docker
    * [Python Flask](https://chentsungyu.github.io/2020/04/26/DevOps/Docker/[DevOps]%20Docker%E5%8C%96%E4%BD%A0%E7%9A%84Python%20Flask%20APP%20%E4%B8%A6%E4%B8%8A%E5%82%B3%E8%87%B3Docker%20Hub/)
* 網頁
    * [Flask 網頁設計](https://ithelp.ithome.com.tw/articles/10258223?sc=pt)

## 未來展望