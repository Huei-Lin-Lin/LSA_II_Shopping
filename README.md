# LSA_II_Shopping
- [Concept Development](#Concept_Develop)
- [安裝 & 設定過程](#install)
- [LSA課堂知識運用](#lsaclass)
- [Job Assignment](#job)
- [References](#referencesa)
- [未來展望](#future)
## 架構
```bash=
.
├── Dockerfile
├── ajax.py
├── requirements.txt
├── start.sh
├── static
│   ├── data
│   │   ├── input.json
│   │   └── message.json
│   ├── jquery-3.6.0.min.js
│   └── script.js
└── templates
    └── data.html  
```

## <a id="Concept_Develop">Concept Development 發展理念</a>

## <a id=install>安裝 & 設定過程</a>
### 基本環境設置
* 作業系統：Linux
* Linux 安裝 Docker
    ```bash=
    sudo apt-get install -y curl
    curl -s https://get.docker.com | sudo sh 
    ```
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
* 以下步驟也可直接從 docker pull
    ```bash=
    docker pull 108213052/flasklsa
    ```
### Flask
* 進入使用者家目錄
    ```bash=
    cd /home/<user>
    ```
* 創建 Flask Application 目錄及基本文件夾結構
    ```bash=
    mkdir -p DFlask/static DFlask/templates 
    ```
* 開始寫網頁
    * data.html 
    * ajax.py
### Docker
* 建立 `Dockerfile` : 建構 container 基本資訊
    * （file 位置`/home/<user>/DFlask/Dockerfile`）
    ```bash=
    vim Dockerfile
    ```
* 創建 `requirements.txt` : 寫入需安裝的 plugin
    ```bash=
    vim requirements.txt
    ```
### 執行
* 創建 `start.sh` : 存放建立 docker image and run container 之指令
    ```bash=
    vim start.sh
    ```
* 啟動
    ```bash=
    bash start.sh
    ```

## <a id='LSAclass'>LSA 課堂知識運用</a>
* [Docker](https://hackmd.io/@ncnu-opensource/book/https%3A%2F%2Fhackmd.io%2F%40108213034%2FB1_qNP2xc#DEMO) : Docker 基本指令


## <a id='job'>Job_Assign</a>

| 組員      | 工作分配 |
| -------- | -------- | 
| 林惠霖    | 後端、爬蟲 | 
| 楊心慈    | 前端、docker |

## <a id='References'>References</a>
* Docker
    * [Python Flask](https://chentsungyu.github.io/2020/04/26/DevOps/Docker/[DevOps]%20Docker%E5%8C%96%E4%BD%A0%E7%9A%84Python%20Flask%20APP%20%E4%B8%A6%E4%B8%8A%E5%82%B3%E8%87%B3Docker%20Hub/)
    * [Build a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-20-04)
* 網頁
    * [Flask 網頁設計](https://ithelp.ithome.com.tw/articles/10258223?sc=pt)

## <a id='future'>未來展望</a>