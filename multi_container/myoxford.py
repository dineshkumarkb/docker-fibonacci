# Generic imports
import requests


class OxfordTest(object):

    def __init__(self,url=None):
        self.url=url

        if self.url is not None:
            self.make_request()

    def make_request(self):
        resp = requests.get(url=self.url)
        print(resp.json())


obj = OxfordTest(url='https://api.github.com/user')