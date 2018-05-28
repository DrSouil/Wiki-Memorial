import requests
from bs4 import BeautifulSoup
link = "https://en.wikipedia.org/wiki/2017"  # 小数据
# https://en.wikipedia.org/wiki/Lists_of_deaths_by_year#2017 # 数据最大
# https://simple.wikipedia.org/wiki/Deaths_in_2017 # 数据中等
r = requests.get(link)
soup = BeautifulSoup(r.text)
soup = soup.find("div", "mw-parser-output")
former = 0
start = False
month = 0
count = 0
f = open("data_2017_name.txt", "a", encoding='utf-8')
for child in soup.children:
    if child.name == "h3" and child.find(id="January_2"):
        start = True
    if child.name == "h2":
        start = False
    if start:
        if child.name == "ul":
            for grandchild in child.find_all("li"):  # li

                for child2 in grandchild.find_all("li"):  # li
                    r2 = requests.get("https://en.wikipedia.org" + child2.a.get('href'))
                    soup2 = BeautifulSoup(r2.text)
                    soup2 = soup2.find(id="mw-content-text")
                    text2 = soup2.get_text()
                    textlenth = len(text2)
                    born = str(child2.find_all("a")[-1].get_text())
                    name = str(child2.find_all("a")[0].get_text())
                    #  print(born)
                    if born.isnumeric():
                        age = 2017 - int(born)
                    else:
                        born = str(child2.find_all("a")[-2].get_text())
                        age = 2017 - int(born)
                    print(str(month) + ',' + str(count) + ',' + str(age) + ',' + str(textlenth)+ ',' +name+ ',' +str(int(born))+ '-' +'2017')
                    f.write(str(month) + ',' + str(count) + ',' + str(age) + ',' + str(textlenth)+ ',' +name+ ',' +str(int(born))+ '-' +'2017' + '\n')
                    count += 1
                    # print(gggrandchild.get_text() + "|" + str(textlenth))
                    # f.write(gggrandchild.get_text() + "|" + str(textlenth) + '\n')
        elif child.name == "h3":
            if child.span.get_text() == 'January':
                month = 1
                count = 0
            elif child.span.get_text() == 'February':
                month = 2
                count = 0
            elif child.span.get_text() == 'March':
                month = 3
                count = 0
            elif child.span.get_text() == 'April':
                month = 4
                count = 0
            elif child.span.get_text() == 'May':
                month = 5
                count = 0
            elif child.span.get_text() == 'June':
                month = 6
                count = 0
            elif child.span.get_text() == 'July':
                month = 7
                count = 0
            elif child.span.get_text() == 'August':
                month = 8
                count = 0
            elif child.span.get_text() == 'September':
                month = 9
                count = 0
            elif child.span.get_text() == 'October':
                month = 10
                count = 0
            elif child.span.get_text() == 'November':
                month = 11
                count = 0
            elif child.span.get_text() == 'December':
                month = 12
                count = 0



f.close()
