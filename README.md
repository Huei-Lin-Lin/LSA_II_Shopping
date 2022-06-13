# LSA_II_Shopping

- [Concept Development](#Concept_Develop)
- [Install & Settings](#install)
- [LSA 課堂知識運用](#lsaclass)
- [Job Assignment](#job)
- [References](#referencesa)
- [未來展望](#future)

## 架構
```bash
.
├── ArrangeData.py
├── Dockerfile
├── README.md
├── VegetableQuotation.py
├── ajax.py
├── crawlerRecipe.py
├── docker-compose.yml
├── driverPath.py
├── requirements.txt
├── static
│   ├── data
│   │   ├── afterRecipeData.json
│   │   ├── quotation.json
│   │   ├── recipeData.json
│   │   └── input.json
│   ├── jquery-3.6.0.min.js
│   └── script.js
├── templates
│   └── data.html
└── testfile
    └── seleniumDockerTest.py
```

## <a id="Concept_Develop">Concept Development</a>
### 起因
隨著畢業季的到來，身邊的朋友將為了前程各奔東西，這可能是大家最後一次見面了
因此，在離開前 MOLi 地縛靈希望能一起吃一頓飯，每個人自己準備一道料理。
但平時大家都只會準備一人份的量，突然要準備那麼多人的份量並計算所花費的價錢，可能都沒有經驗，所以我們想試試看能不能做出能讓人根據菜單及人數推估出來食材份量及總花費的網頁工具。

### 功能
* 查詢料理方式
* 列出食材清單
* 提供食材現價

## <a id=install>Install & Settings</a>
### 基本環境設置
* 作業系統：Linux
* [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
* [Install Docker Compose CLI plugin](https://docs.docker.com/compose/install/compose-plugin/#install-the-plugin-manually)
* 在本機測試的話，需另外安裝 selenium & flask
    <details>
    <summary>安裝方法</summary>
    
    ### selenium
    * 安裝指令
        ```bash=
        pip3 install selenium
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
            ![](https://i.imgur.com/4dc1LRr.png|width=70)
    * 進入此[連結](https://sites.google.com/chromium.org/driver/)選擇跟瀏覽器相同的版本
    ![](https://i.imgur.com/34eXpKM.png)
    * 選擇跟自己作業系統相同的壓縮檔
        ![](https://i.imgur.com/K5vkSkE.png|width=70)
    * 解壓縮 
        ![](https://i.imgur.com/NQzTFiM.png|width=70)
    * 選擇檔案要放在哪個路徑下，**要記好這個路徑在哪，等下要用到**
        ![](https://i.imgur.com/IEeAJ6u.png|width=70)
    * 把這個路徑放到 `crawlerRecipe.py`、`VegetableQuotation.py` 兩個檔案中
        * `crawlerRecipe.py`![](https://i.imgur.com/J4qdAZd.png|width=70)
        * `VegetableQuotation.py`![](https://i.imgur.com/3EGQpzs.png|width=70)

    ### Flask
    * 安裝指令
        ```bash=
        pip3 install flask
        ```
    * 進入使用者家目錄
        ```bash=
        cd /home/<user>
        ```
    * 創建 Flask Application 目錄及基本文件夾結構
        ```bash=
        mkdir -p DFlask/static DFlask/templates 
        ```
    * 開始用 Flask 寫網頁
    </details>

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
### docker-compose
* 建立 `docker-compose.yml` 
    * （file 位置 `/home/<user>/DFlask/compose.yml`）
    ```bash=
    vim docker-compose.yml
    ```
* 創建 docker-compose
    ```bash=
    docker-compose build
    ```
* 啟動 docker-compose
    ```bash=
    docker-compose up
    ```
* 查看 port
    * `4444`: selenium chrome session
    * `5000/data`: 網頁畫面
    * `7900`: 密碼:`secret`, 顯示爬蟲時的網頁畫面 (:cool:超酷！！)
* 結束
    ```bash=
    Control + C
    or
    docker-compose down
    ```
    

## <a id='LSAclass'>LSA 課堂知識運用</a>
* 執行 docker-compose
    1. 將 gitnub 的檔案 pull 下來
    2. 創建並啟動 docker-compose services
        ```bash=
        docker-compose build
        docker-compose up
        ```
    3. 可查看 port
        * `4444`: selenium chrome session
        * `5000/data`: 網頁畫面
        * `7900`: 密碼:`secret`, 顯示爬蟲時的網頁畫面 (超酷！！)
* Docker : 
    * [Docker 基本指令](https://hackmd.io/@ncnu-opensource/book/https%3A%2F%2Fhackmd.io%2F%40108213034%2FB1_qNP2xc#DEMO)
    * 下載 images 並啟動
        ```bash=
        docker pull selenium/standalone-chrome
        docker run -d selenium/standalone-chrome
        ```
    * 進入 container 編輯 :
        ```bash=
        docker exec -it <containerID> bash
        cd /home/<user>/
        sudo apt-get update
        sudo apt-get install vim
        sudo apt-get install pip
        pip install selenium
        pip install flask
        ```
    * 刪除所有 container :
        ```bash=
        docker pa -a
        ```
    * 查看所有已 stop 的 container :
        ```bash=
        docker container prune
        ```
    * docker remove `<none>` images : 
        ```bash=
        docker image prune --filter="dangling=true"
        ```
* docker-compose : 
    * 建立並啟動 docker-compose
        ```bash=
        docker-compose up -d --build
        ```
    * 查看 docker-compose
        ```bash=
        docker-compose ps
        ```
    * 結束並刪除 docker-compose
        ```bash=
        docker-compose down
        ```
* 基本指令
    * directory 複製 :
        ```bash=
        cp -a <source>/. <destination>
        ```
    * directory or file rename :
        ```bash=
        mv <old_name> <new_name>
        ```


## <a id='job'>Job_Assign</a>

| 組員      | 工作分配 |
| -------- | -------- | 
| 林惠霖    | Selenium | 
| 楊心慈    | Docker, Flask |

## <a id='References'>References</a>
* Docker
    * [Python Flask](https://chentsungyu.github.io/2020/04/26/DevOps/Docker/[DevOps]%20Docker%E5%8C%96%E4%BD%A0%E7%9A%84Python%20Flask%20APP%20%E4%B8%A6%E4%B8%8A%E5%82%B3%E8%87%B3Docker%20Hub/)
    * [Build a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-20-04)
    * [Run Selenium Tests in Docker](https://www.browserstack.com/guide/run-selenium-tests-in-docker)
    * [Compose file build reference](https://docs.docker.com/compose/compose-file/build/)
* docker-compose
    * [Compose file build reference](https://docs.docker.com/compose/compose-file/build/)
    * [SeleniumHQ
](https://github.com/SeleniumHQ/docker-selenium)
    * [Flask+Redis 多服務開發部署 docker compose](https://www.youtube.com/watch?v=lXuw2sncltE&t=371s)
* 網頁
    * [Flask 網頁設計](https://ithelp.ithome.com.tw/articles/10258223?sc=pt)
    * [selenium 網頁自動化、網路爬蟲](https://www.youtube.com/watch?v=ximjGyZ93YQ&t=1362s&ab_channel=GrandmaCan-%E6%88%91%E9%98%BF%E5%AC%A4%E9%83%BD%E6%9C%83)

## <a id='future'>未來展望</a>
* 單次記帳
* 會員
* 把估價內容寄到自己的信箱