# LSA_II_Shopping

# 買菜網
## Concept Development 理念
隨著畢業季的到來，身邊的朋友將為了前程各奔東西，這可能是大家最後一次見面了
因此，在離開前 MOLi 地縛靈希望能一起吃一頓飯，每個人自己準備一道料理。
但平時大家都只會準備一人份的量，突然要準備那麼多人的份量並計算所花費的價錢，可能都沒有經驗，所以我們想試試看能不能做出能讓人根據菜單及人數推估出來食材份量及總花費的網頁工具。

## Implementation Resources 設備資源
* 作業系統是 Linux 的電腦

## Existing Library/Software
* 爬蟲：Selenium
* 架網站：Python Flask
* 網頁前端框架：Flat UI
* 部屬網站：Docker
* 資料庫：MySQL
* 資料庫管理工具：phpMyAdmin

## Implementation Process 實作過程
1. 寫爬蟲程式爬食譜、菜價網站
2. 建資料庫
3. 寫前端網頁
4. 前後端整合
5. 把網站架到 Docker 上
6. 部屬
7. 使用

## Installation 安裝
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
    * 網頁畫面
        * `http://{your IP}:5000`
    * 顯示爬蟲時的網頁畫面
        * `http://{your IP}:7900`
        * 密碼：`secret` 
    * phpMyAdmin，查看資料庫
        * `http://{your IP}:8080`
6. 結束服務
    * `docker compose down`

## Job Assignment 工作分配
| 組員      | 工作分配 |
| -------- | -------- | 
| 林惠霖    | 爬蟲、後端 | 
| 楊心慈    | Docker、前端 |

## References 參考資料
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