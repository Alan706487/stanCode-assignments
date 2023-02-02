"""
File: webcrawler.py
Name: Alan
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': "t-stripe"})
        m_num = 0
        f_num = 0
        m = 2
        f = 4

        # 修正後的
        # for tag in tags:
        #     tag = tag.tbody.text.split()  # tag = ['1', 'Jacob', '273,945', 'Emily', '223,723', '2'...]
        #     for i in range(200):
        #         m_num += int(tag[m].replace(',', ''))
        #         f_num += int(tag[f].replace(',', ''))
        #         m += 5
        #         f += 5
        # print(f'Male number: {m_num}\nFemale number: {f_num}')


        tags = soup.find_all('td')
        m_num = 0
        f_num = 0
        mix_num_lis = []  # 先把男女的人數都加進串列 元素是字串 之後再用奇偶索引判斷男女
        for i in range(1, len(tags) - 2):  # tags裡的元素才有.text  得乾淨的排名 名字 人數
            ele = tags[i].text.split(' ')[0]  # 取出tags裡第i個元素
            next_ele = tags[i + 1].text.split(' ')[0]  # 取出tags裡第i+1個元素
            if ele.isalpha():  # 把男和女後面的排名取出包成串列
                mix_num_lis.append(next_ele)  # ['num', 'num', ...] 但num含有標點
        for i in range(len(mix_num_lis)):
            if i % 2 == 0:  # male num 在 mix_num_lis 的偶數位 反之在奇數
                m_num += int(mix_num_lis[i].replace(',', ''))  # .replace(',', '')刪掉標點符號
            else:
                f_num += int(mix_num_lis[i].replace(',', ''))
        print(f'Male number: {m_num}\nFemale number: {f_num}')


if __name__ == '__main__':
    main()
