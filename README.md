# beijing-paralympic-2022-rank-spider
一个可以从北京2022官方网站爬取冬残奥会国家排名的Python程序 A python programme that can scrap Beijing paralympic 2022 country rank from Beijing2022 Official Website

## 中文文档
懒得写文档了。。。。
总之，就是一个差不多能从beijing2022官方网站爬取国家排名的小东西
用beautifulsoup爬虫爬取信息，然后用flask做服务端，jinja2模板渲染
一个加急写的小烂活，凑合看吧
server.py是存放爬虫和服务器东西的，templates文件夹下的main.html就是前端页面了
运行整个程序要先运行server.py,然后复制输出中的地址到网页栏里
Montserrat的ttf文件是字体
PS:这个东西实际上是一个学校项目

## English Document
Lazy to write this document....
Overall, is just a little thing that can scrap country's rank from beijing2022 official website..
Use beautifulsoup to scrap things, and use flask to do the server, jinja2 render
A mini, rubbish project, just make do with it.
server.py stores all scrap and server stuffs, and main.html under templates folder is the frontend page.
You need to first run server.py in order to run the whole thing, then copy the address into your address bar in the browser.
ttf file which is called Montserrat is the font.
PS:This thing is actually a school project
