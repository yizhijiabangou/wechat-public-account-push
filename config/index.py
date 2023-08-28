import requests
import json

def f_pachong(key):
    url = 'https://www.sogou.com/web?'
    param = {'query': key}
    header = {'ser-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}
    result = requests.get(url=url, params=param, headers=header)
    # file_name = "file_" + key + ".html"
    file_name = 'file_dashuju.html'
    with open(file_name, 'w', encoding='utf-8')as f:
        f.write(result.text)


def test_fanyi(word):
    url = '	https://fanyi.sogou.com/reventondc/suggV3'
    header = {'ser-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}
    param = {
        "from": "auto",
        "to": "zh-CHS",
        "client": "web",
        "text": word,
        "uuid": "2653897f-5386-43f7-9961-c931e7258321",
        "pid": "sogou-dict-vr",
        "addSugg": "on"
        }
    result = requests.post(url=url, data=param, headers=header)
    file_name = "file_" + word + ".json"
    json_file = open(file_name, 'w', encoding='utf-8')
    json.dump(obj=result.json(), fp=json_file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    # key = input("请输入搜索关键字：")
    # f_pachong(key)
    word = input("请输入要翻译的单词：")
    test_fanyi(word)