import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

# 列表，用于存放结果
country_list = []


# Spider 爬取数据
def spider():
    html = requests.get(
        "https://results.beijing2022.cn/beijing-2022/paralympic-games/en/results/all-sports/medal-standings.htm")
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    print(soup.prettify())
    # 爬取前十个国家的数据
    for i in range(0, 10):
        countries = soup.find_all('abbr')[i].get_text()
        country_list.append(countries)


spider()
# 检测结果
print(country_list)
# END OF SPIDER


# Flask服务端，渲染内容
app = Flask(__name__)
app.debug = True


@app.route("/")
def main():
    return render_template("main.html", country_list=country_list)


# RUN APP
app.run(host="127.0.0.1", port=5000)
