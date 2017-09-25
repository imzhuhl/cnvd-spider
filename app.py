#!/usr/bin/python
# -*- coding: utf-8 -*-

'''requirements
python3

requests
openpyxl
beautifulsoup
selenium

Chrome
ChromeDriver: http://npm.taobao.org/mirrors/chromedriver
'''

import requests, time, openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
import argparse

import config


# return url list from every page
def get_detail_url_list(main_url, page_num):
    # page1 offset=0; page2 offset=20; page3 offset=40; ....
    offset = str(page_num * 20)
    while True:
        try:
            r = requests.get(main_url + offset)
        except:
            print("connection error, url: {0}\nwait 10s and try again".format(main_url + offset))
            time.sleep(10)
            continue
        if r.status_code != 200:
            print("{0} ==> response: {1}, try again".format(main_url + offset, r.status_code))
            time.sleep(2)
            continue
        break

    soup = BeautifulSoup(r.text, 'lxml')

    tags = soup.find('tbody', id='tr').find_all('a')
    url_detail_list = []
    for tag in tags:
        url_detail_list.append(tag.attrs['href'])
    return url_detail_list

# return detailed information of one flaw
def get_one_info(url):
    print(url)
    if('http' not in url):
        return
    info = []

    while True:
        try:
            r = requests.get(url, headers=config.headers, cookies=config.cookies)
        except:
            print("connection error, url: {0}\nwait 10s and try again".format(url))
            time.sleep(10)
            continue
        if r.status_code != 200:
            print("detailed page ==> response: {0}, change cookies...".format(r.status_code))
            time.sleep(2)
            change_cookies()
            continue
        break

    soup = BeautifulSoup(r.text, 'lxml')
    title = soup.find('h1').text
    info.append(title)

    trs = soup.find('tbody').find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        label = tds[0].text
        if label in config.demand_list:
            s = config.selector[label](tds[1])
            info.append(s)

    return info

# update cookies
def change_cookies():
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    browser = webdriver.Chrome(chrome_options=options)
    browser.get('http://www.cnvd.org.cn/flaw/show/CNVD-2017-26804')
    cookies_list = browser.get_cookies()
    for c in cookies_list:
        config.cookies[c['name']] = c['value']

    browser.close()


if __name__ == '__main__':
    # deal input
    parser = argparse.ArgumentParser(usage='usage -p <page count>')
    parser.add_argument("-p", dest="page_count")
    p_c = parser.parse_args().page_count
    if p_c == None:
        print("default page count is 60, 1200 information (y/n) : ", end='')
        n = input()
        if n in ['y', 'yse', 'Y', 'YES']:
            p_c = 60
        else:
            exit(0)

    # init excel
    wb = openpyxl.Workbook()
    ws = wb.get_active_sheet()
    ws.title = "info"
    ws.cell(row=1, column=1).value = '标题'
    for i in range(len(config.demand_list)):
        ws.cell(row=1, column=i+2).value = config.demand_list[i]

    # crawl
    main_url = 'http://ics.cnvd.org.cn/?max=20&offset='
    for i in range(int(p_c)):
        url_list = get_detail_url_list(main_url, i)
        for j in range(len(url_list)):
            info = get_one_info(url_list[j])
            if info == '':
                continue
            _row = i * 20 + j + 2
            for k in range(len(info)):
                ws.cell(row=_row, column=k+1).value = info[k]

    # result file
    wb.save(filename="./result/test.xlsx")
