from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl

options=Options()
options.add_argument('--headless')
driver = webdriver.Chrome('chromedriver',options=options)
driver.get('https://www.google.co.jp')

def search_func(keyword):
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys(keyword)
    search_bar.submit()
def find_func():
    result_list = []
    try:
        for elem_h3 in driver.find_elements_by_xpath('//a/h3'):
            elem_a = elem_h3.find_element_by_xpath('..')
            site_title = elem_h3.text
            url = elem_a.get_attribute('href')
            result_list.append([site_title,url])
    except:
        pass
    return result_list
def next_page_func():
    try:
        next_link = driver.find_element_by_id('pnnext')
        driver.get(next_link.get_attribute('href'))
    except:
        raise Stop

search_list = []
keyword = "python"
search_func(keyword)
for i in range(6):
    for j in find_func():
        search_list.append(j)

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'result'
sheet['A1'] = keyword
sheet['A2'] = 'サイト名'
sheet['B2'] = 'URL'

for k in range(len(search_list)):
    title_place = "A{}".format(k+3)
    url_place = "B{}".format(k+3)
    sheet[title_place] = search_list[k][0]
    sheet[url_place] = search_list[k][1]

wb.save('search_result.xlsx')

