import json

import requests


# url='https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?&start={}&count={}&loc_id=108288'


class Xiaolu(object):
    def __init__(self):
        self.url = 'https://www.xiaoluxuanfang.com/api/v4/search/houses'
        self.headers = {
            # 'Referer': 'https://m.douban.com/movie/nowintheater?loc_id=108288',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            "Content-Type": "application/json"
        }

    def get_data_from_url(self,i):
        s = {"query": {"key": "defaultText", "parentKey": "cityCode", "parentValue": "440300", "type": "sell"},
             "sorts": [{"key": "sort", "value": "{\"default\":0}"}], "sinceId": i, "size": 20}

        s = json.dumps(s)

        data = requests.post(self.url, data=s, headers=self.headers).text
        return data

    def parse_data(self, data):
        new_data = json.loads(data)
        dict_data = new_data['result']
        print(dict_data)
        return dict_data
    def save_data(self, dict_data):
        with open('xiaolukanfang.txt', 'a', encoding='utf8') as f:
            for i in dict_data:
                json.dump(i, f, ensure_ascii=False)
                f.write('\n')

    def run(self):
        for i in range(1,153):
            data=self.get_data_from_url(i)
            dict_data=self.parse_data(data)
            self.save_data(dict_data)
if __name__ == '__main__':
   xiao=Xiaolu()
   xiao.run()