import requests
from bs4 import BeautifulSoup

cloak_url = 'https://cloak.pia.jp/resale/item/list?areaCd=&prefectureCd=&hideprefectures=01&perfFromDate=&perfToDate=&numSht=&priceFrom=&priceTo=&eventCd=2209305%2C2209306%2C2209307&perfCd=&rlsCd=&lotRlsCd=&eventPerfCdList=&stkStkndCd=&stkCliCd=&invalidCondition=&preAreaCd=&prePrefectureCd=&totalCount=40&beforeSearchCondition=%7B%22event_cd%22%3A%222209305%2C2209306%2C2209307%22%2C%22sort_condition%22%3A%22perf_date_time%2Casc%22%2C%22page%22%3A1%7D&ma_token=96r4j5mxIQ6JnHd&sortCondition=entry_date_time%2Cdesc'

def get_elems():
    response = requests.get(cloak_url)
    soup = BeautifulSoup(response.text,'html.parser')
    header_elems = soup.find_all(class_='item_header_info')
    ticket_elems = soup.find_all(class_='item_result_box_msg')
    header_elems = get_text_list(header_elems)
    ticket_elems = get_text_list(ticket_elems)
    return join(header_elems,ticket_elems)


def join(arr1,arr2):
    new_arr = []
    for i, e in enumerate(arr1):
        e = format(e)
        arr2[i] = format(arr2[i])
        new_arr.append([e,arr2[i]])
    return new_arr

def get_text_list(elems):
    new_elems = []
    for e in elems:
        e = e.text
        new_elems.append(e)
    return new_elems

def format(s):
    s = s[1:-1]
    s = s.replace('\n\xa0\xa0\n\n\n\n／\n',' / ')
    s = s.replace('\xa0','')
    for i in range(3):
        s = s.replace('\n\n','\n')
    return s
    