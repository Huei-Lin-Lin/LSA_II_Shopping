# LSA_II_Shopping
- [Concept Development](#Concept_Develop)
- [Install & Settings](#install)
- [LSA 課堂知識運用](#lsaclass)
- [Job Assignment](#job)
- [References](#referencesa)
- [未來展望](#future)

## 架構
```bash
. DFflask
├── Dockerfile
├── ajax.py
├── crawlerBeautifulSoup.py
├── crawlerRecipe.py
├── docker-compose.yml
├── requirements.txt
├── seleniumDockerTest.py
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
### 起因
隨著畢業季的到來，身邊的朋友將為了前程各奔東西，這可能是大家最後一次見面了
因此，在離開前 MOLi 地縛靈希望能一起吃一頓飯，每個人自己準備一道料理。
但平時大家都只會準備一人份的量，突然要準備那麼多人的份量並計算所花費的價錢，可能都沒有經驗，所以我們想試試看能不能做出能讓人根據菜單及人數推估出來食材份量及總花費的網頁工具。

### 功能
* 查詢料理方式
* 列出食材清單
* 提供食材現價

## <a id=install>安裝 & 設定過程</a>
### 基本環境設置
* 作業系統：Linux
* [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
* [Install Docker Compose CLI plugin](https://docs.docker.com/compose/install/compose-plugin/#install-the-plugin-manually)
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
    * 先查看瀏覽器的版本 : 左上角的三個圓點 :point_right: 說明 :point_right: 關於 Google Chrome
        ![](https://i.imgur.com/ZgGJlbt.png)
        ![](https://i.imgur.com/4dc1LRr.png)
    * 進入此[連結](https://sites.google.com/chromium.org/driver/)下載 ChromeDriver
    ![](https://i.imgur.com/34eXpKM.png)
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
    * （file 位置 `/home/<user>/DFlask/Dockerfile`）
    ```bash=
    vim Dockerfile
    ```
* 創建 `requirements.txt` : 寫入需安裝的 plugin
    * （file 位置 `/home/<user>/DFlask/requirements.txt`）
    ```bash=
    vim requirements.txt
    ```
### 執行
* 創建 `start.sh` : 存放建立 docker image and run container 之指令
    * （file 位置 `/home/<user>/DFlask/start.sh`）
    ```bash=
    vim start.sh
    ```
* 啟動
    ```bash=
    bash start.sh
    ```

## <a id='LSAclass'>LSA 課堂知識運用</a>
* [Docker](https://hackmd.io/@ncnu-opensource/book/https%3A%2F%2Fhackmd.io%2F%40108213034%2FB1_qNP2xc#DEMO) : Docker 基本指令
    * docker remove none images : `docker image prune --filter="dangling=true"`
    * container : `sudo apt-get update`、`sudo apt-get install vim`
* directory 複製 : `cp -a <source>/. <destination>`


## <a id='job'>Job_Assign</a>

| 組員      | 工作分配 |
| -------- | -------- | 
| 林惠霖    | 後端、爬蟲 | 
| 楊心慈    | 前端、docker |

## <a id='References'>References</a>
* Docker
    * [Python Flask](https://chentsungyu.github.io/2020/04/26/DevOps/Docker/[DevOps]%20Docker%E5%8C%96%E4%BD%A0%E7%9A%84Python%20Flask%20APP%20%E4%B8%A6%E4%B8%8A%E5%82%B3%E8%87%B3Docker%20Hub/)
    * [Build a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-20-04)
    * [Run Selenium Tests in Docker](https://www.browserstack.com/guide/run-selenium-tests-in-docker)
    * [Compose file build reference](https://docs.docker.com/compose/compose-file/build/)
* 網頁
    * [Flask 網頁設計](https://ithelp.ithome.com.tw/articles/10258223?sc=pt)

## <a id='future'>未來展望</a>
* 單次記帳
* 會員
* 把估價內容寄到自己的信箱