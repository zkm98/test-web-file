from bs4 import BeautifulSoup
import requests, sys

class downloader(object):

    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/0_243/'
        self.names = []       
        self.urls = []          
        self.nums = 0          


    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[15:])                           
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('start:')
    for i in range(dl.nums):
        dl.writer(dl.names[i], 'a.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write(" already downloaded:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('already down')
