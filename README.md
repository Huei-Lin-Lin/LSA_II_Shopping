# LSA_II_Shopping

# 買菜網
## Concept Development 
隨著畢業季的到來，身邊的朋友將為了前程各奔東西，這可能是大家最後一次見面了
因此，在離開前 MOLi 地縛靈希望能一起吃一頓飯，每個人自己準備一道料理。
但平時大家都只會準備一人份的量，突然要準備那麼多人的份量並計算所花費的價錢，可能都沒有經驗，所以我們想試試看能不能做出能讓人根據菜單及人數推估出來食材份量及總花費的網頁工具。

## Implementation Resources 
* 作業系統是 Linux 的電腦

## Existing Library/Software
* 爬蟲：Selenium
* 架網站：Python Flask
* 網頁前端框架：Flat UI
* 部屬網站：Docker
* 資料庫：MySQL
* 資料庫管理工具：phpMyAdmin

## Implementation Process 
1. 寫爬蟲程式爬食譜、菜價網站
2. 建資料庫
3. 寫前端網頁
4. 前後端整合
5. 把網站架到 Docker 上
6. 部屬
7. 使用

## Installation 
1. [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
    * `sudo apt-get update`
    * `sudo apt-get install \ ca-certificates \ curl \ gnupg \ lsb-release`
    * `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg`
    * `echo \ "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \ $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`
    * `sudo apt-get update`
    * `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin`
    * `apt-cache madison docker-ce`
    * `sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io docker-compose-plugin`
2. [Install Docker Compose CLI plugin](https://docs.docker.com/compose/install/compose-plugin/#install-the-plugin-manually)
    * `sudo apt-get update`
    * `sudo apt-get install docker-compose-plugin`
    * `apt-cache madison docker-compose-plugin`
    * `sudo apt-get install docker-compose-plugin=<VERSION_STRING>`
    * `docker compose version`
3. 下載 GitHub 專案
    * `git clone https://github.com/miga-666/automatedSquid.git`
4. 啟動服務
    * `docker compose build`
    * `docker compose up`
5. 可查看以下 port
    * selenium chrome session
        * `http://{your IP}:4444`
        * ![](https://i.imgur.com/myb0WQN.png)
    * 網頁畫面
        * `http://{your IP}:5000`
        * ![](https://i.imgur.com/6wC4nVx.png)
        * 輸入料理資料
        * ![](https://i.imgur.com/975V8GD.png)
        * 顯示爬蟲結果
        * ![](https://i.imgur.com/q7YUMe4.png)
    * 顯示爬蟲時的網頁畫面
        * `http://{your IP}:7900`
        * ![](https://i.imgur.com/pqH6OaU.png)
        * 密碼：`secret` 
        * ![](https://i.imgur.com/CmKb6ci.png)
        * 爬蟲畫面
        * ![](https://i.imgur.com/gYSA9QE.png)
    * phpMyAdmin，查看資料庫
        * `http://{your IP}:8080`
        * 帳號：root
        * 密碼：root
        * ![](https://i.imgur.com/1NuoLvl.png)
        * lsa2 資料庫下的 foodprice 資料表是我們部分菜價
        * ![](https://i.imgur.com/LHC7Ara.png)
6. 結束服務
    * `docker compose down`
* [實作影片連結](https://www.youtube.com/watch?v=jGRvM7-slok&ab_channel=%E6%A5%8A%E5%BF%83%E6%85%88)

## 補充：如果想要更換資料表的內容
### 方法一：直接修改
* 連線至 `http://127.0.0.1:8080`
* 帳號：`root`
* 密碼：`root`
* 直接新增或修改資料
    * ![](https://i.imgur.com/i2ikAKe.png)
### 方法二：匯入 `.sql` 檔
* 在 `/home/<user>/<dir_name>/app/db/` 下匯入 `<要更換資料表內容的檔案>.sql` 
* `vim <要更換資料表內容的檔案>.sql`
    * 在最上方新增
    ```sql=
    create database lsa2;
    use lsa2;
    ```
    * 意思是建立一個名字叫 `lsa2` 的資料庫
* `vim operationDB.py`，修改資料表名稱
    * (file 位置 : `/home/<user>/<dir_name>/app/db/`)
    ```python=
    import connectDB

    # 查詢資料庫菜價
    def queryFoodPrice(str):
        mydb = connectDB.connect() # 連接 DB，讓資料自動組織成字典
        cursor = mydb.cursor(dictionary = True)
        sql = 'select * from <資料表名稱> WHERE foodName LIKE \'%{str}%\' '.format(str=str) # 定義 SQL 語句
        cursor.execute(sql) # 執行 SQL 語句
        result = cursor.fetchall() # 獲取返回結果
        cursor.close()
        mydb.close()
        return result
    ```

## LSA 課堂知識運用
* Docker : 
    * [Docker 基本指令](https://hackmd.io/@ncnu-opensource/book/https%3A%2F%2Fhackmd.io%2F%40108213034%2FB1_qNP2xc#DEMO)
    * 下載 images 並啟動
        ```bash=
        docker pull <image_name>
        docker run <image_name>
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
        ......
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

## 遇到的問題
* 中文數字
    * 例如： 2 顆番茄、一匙醬油
* 虛擬機效能較差，導致超時，爬蟲爬不到東西
    * 解決方法：跟有 Linux 作業系統的同學借電腦測試、用跟學校申請的伺服器測試
        > 感謝鄭采禎、陳琪樺 :heart:
* Service 在本機環境與 container 環境的安裝設定差異
* docker-compose service 啟動速度的差異

## 感謝名單
* 題材發想：[李漢偉](https://github.com/UncleHanWei)、蔣毓婷、陳柏瑋 
* 電腦支援：鄭采禎、陳琪樺

## Job Assignment 
| 組員      | 工作分配 |
| -------- | -------- | 
| 林惠霖    | 爬蟲、後端 | 
| 楊心慈    | Docker、前端 |

## References 
* Selenium
    * [【python】selenium 網頁自動化、網路爬蟲](https://www.youtube.com/watch?v=ximjGyZ93YQ&t=418s&ab_channel=GrandmaCan-%E6%88%91%E9%98%BF%E5%AC%A4%E9%83%BD%E6%9C%83) 
    * [Selenium with Python](https://selenium-python.readthedocs.io/)
    * [Selenium 啟動 Chrome 配置參數問題](https://zhuanlan.zhihu.com/p/60852696)
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
* DataBase
    * [Deploy Flask-MySQL app with docker-compose](https://www.devopsroles.com/deploy-flask-mysql-app-with-docker-compose/)