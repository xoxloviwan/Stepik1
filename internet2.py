import re
import requests

# import sys
#
# sys.stdin = open("C:/Users/xoxlo/Desktop/tester.txt",'r')
link_pattern = re.compile(r'<a[^>]*?href=[\'\"]?'
                          r'(?:.*://)?'
                          r'(\w[\w.\-]*)')
res = requests.get(input())
links = set()
for line in res.text.splitlines():
    line = line.rstrip()
    link = re.findall(link_pattern, line)
    if link:
        links.add(*link)
lst = list()
for link in links:
    lst.append(link)
lst.sort()
for el in lst:
    print(el)

# http://pastebin.com/raw/7543p0ns
