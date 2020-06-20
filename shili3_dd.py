# 嵩天MOOC 第三周8单元
import requests
import re
# url = 'http://search.dangdang.com/?key=Python&act=input&page_index=2#J_tab'
# kvh = {'user-agent': 'Mozillia/5.0'}
# print('{:3}'.format('zhang'))

def getHTMLText(url):
    try:
        print('开始读取网页')
        r = requests.get(url, timeout = 30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('Failed in getHTMLText!')
        return ''

def parsePage(ilt, html):
    try:
        tlt = re.findall('id=\"p[\d]*\".*?title=\".*?\"', html, flags=re.S) #必须加re.S后.才能配换行符
        # print('tlt:', tlt)
        plt = re.findall('id=\"p[\d]*\".*?&yen;[\d\.]*?<', html, flags=re.S)
        # print('plt:', plt)
        for i in range(len(tlt)):
            title = eval(tlt[i].split('=')[2])  # eval函数可以去掉外部引号
            price = (plt[i].split(r';')[1])
            price = re.sub('<', '元', price)
            ilt.append([title, price])
    except:
        print('Failed in parsePage!')

def printGoodslist(ilt):
    tplt = '{:4}\t{:^40}\t{:>8}'
    print(tplt.format('序号', '书名', '价格'))
    count = 0
    try:
        for g in ilt:
            count = count + 1
            print(tplt.format(count, g[0], g[1]))
    except:
        print('Failed in printGoodslist!')

def main():
    goods = '哲学'
    depth = 1
    infolist = []
    for i in range(depth):
        pnum = i+1
        try:
            url = 'http://search.dangdang.com/?key='+goods+'&act=input&page_index='+str(pnum)+'#J_tab'
            html = getHTMLText(url)
            parsePage(infolist, html)
        except:
            continue
    printGoodslist(infolist)

main()