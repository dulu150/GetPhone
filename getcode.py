from selenium import webdriver
import time
from ahk import AHK

base_url = 'https://leetcode-cn.com'

name_list = []
url_list = []
global browser
def GetAllItemNameAndUrl():
    global browser
    options = webdriver.ChromeOptions()
    options.add_argument('--save-page-as-mhtml')
    browser = webdriver.Chrome(chrome_options=options)

    browser.get(base_url +  '/problemset/all/')
    print(base_url +  '/problemset/all/')

    #input()
    browser.implicitly_wait(7)

    table = browser.find_elements_by_tag_name("table")[0]
    tbody = table.find_element_by_tag_name("tbody")
    tr_list = tbody.find_elements_by_tag_name("tr")
    print("共有", len(tr_list))
    global name_list
    global url_list
    for i in range(len(tr_list)):
        tr = tr_list[i]
        tds = tr.find_elements_by_tag_name("td")
        td = tds[2]
        name_and_url = td.find_elements_by_tag_name("a")[0]
        url = name_and_url.get_attribute("href")
        name = name_and_url.get_attribute("innerText")
        global name_list
        global url_list
        url_list.append(url)
        name_list.append(name)
        if i % 99 == 0:
            print("处理了", i, "个")
    print("实际获取到", len(url_list), "个题目信息")
    return len(url_list)


def GetItemDsc(itemindex):
    global browser
    js = 'window.open("' + url_list[itemindex] + '")'
    print(js)
    browser.execute_script(js)
    browser.implicitly_wait(7)
    browser.switch_to.window(browser.window_handles[1])
    dsc = browser.find_elements_by_class_name("notranslate")[0]
    item_text = dsc.get_attribute("innerText")
    print(item_text)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    return

def GetAnswerFromUrl(url):
    global browser
    js = 'window.open("' + url + '")'
    print(js)
    browser.execute_script(js)
    browser.implicitly_wait(7)
    browser.switch_to.window(browser.window_handles[1])

    time.sleep(3)
    ahk = AHK()
    old_pos = ahk.mouse_position = (600, 180)
    ahk.right_click()
    time.sleep(1)
    ahk.mouse_position = (old_pos[0] + 50, old_pos[1] + 100)
    ahk.click()
    time.sleep(0.5)
    ahk.key_press('Enter')
    time.sleep(2)

    browser.close()
    browser.switch_to.window(browser.window_handles[0])

def GetItemAnswer(itemindex):
    global browser
    js = 'window.open("' + url_list[itemindex] + '/solution' + '")'
    print(js)
    browser.execute_script(js)
    browser.implicitly_wait(7)
    browser.switch_to.window(browser.window_handles[1])

    time.sleep(2)
    div = browser.find_elements_by_class_name("css-ym6w1n-SolutionWrapper")[0]
    div = div.find_elements_by_tag_name("div")[2]
    div = div.find_elements_by_tag_name("div")[0]
    div = div.find_elements_by_tag_name("div")[0]
    div = div.find_elements_by_tag_name("div")[0]
    div = div.find_elements_by_tag_name("div")[1]
    a = div.find_elements_by_tag_name("a")[1]

    url = a.get_attribute("href")
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

    GetAnswerFromUrl(url)
    return

def GetAnswerFromUrlTest():
    global browser
    optionsx = webdriver.ChromeOptions()
    optionsx.add_argument('--save-page-as-mhtml')
    browser = webdriver.Chrome(options=optionsx)

    browser.get("https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-2/")
    browser.implicitly_wait(7)

    ahk = AHK()
    old_pos = ahk.mouse_position = (600, 180)
    ahk.right_click()
    ahk.mouse_position = (old_pos[0] + 50, old_pos[1] + 100)
    ahk.click()
    time.sleep(0.5)
    ahk.key_press('Enter')
    time.sleep(2)
    browser.close()

if __name__ == '__main__':
    total_num = GetAllItemNameAndUrl()
    GetItemDsc(0)
    GetItemAnswer(0)

    GetItemDsc(1)
    GetItemAnswer(1)

    global browser
    browser.close()
