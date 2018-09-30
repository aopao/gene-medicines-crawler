# gene-medicines-crawler
一个爬取药品的爬虫，只限于和精准用药相关的药品  
1.安装scrapy  
sudo apt-get install python-pip python-lxml python-crypto python-cssselect python-openssl python-w3lib python-twisted python-dev libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev  
sudo pip install scrapy  
2.运行  
scrapy crawl snpedia -o gene-medicines.csv  
