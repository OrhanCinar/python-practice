import http.client
from html.parser import HTMLParser
import requests

# conn = http.client.HTTPConnection('www.google.com')
# conn.request('GET', "/")
# response = conn.getresponse()
# print(response.read())
# data = response.read()

r = requests.get('http://www.google.com')
# print(r.text)

links = []


class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print(type(tag))
        if tag == 'td' or tag == 'a':
            #print(attrs[-1], dir(attrs))
            attr = dict(attrs)
            links.append(attr)
        if tag == 'a' and 'href' in attrs and self.extracting:
            #print('start', tag, attrs['href'])
            pass

    def handle_endtag(self, tag):
        pass
        # print('end', tag)

    def handle_data(self, tag):
        pass
        # print('data', tag)


parser = MyHtmlParser()

# print(parser.feed(r.text))
parser.feed(r.text)

for l in links:
    print(l.get('href'), "")
