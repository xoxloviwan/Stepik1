import re
import requests

# import sys
#
# sys.stdin = open("C:/Users/xoxlo/Desktop/tester.txt",'r')
link_pattern = re.compile(r'(?:<a[^>]*?href=[\'\"]?)'
                          r'(?:\w*?://)'
                          r'(\w[\w\.\-]*)')
res = requests.get(input())
domains = set()
for line in res.text.splitlines():
    line = line.rstrip()
    links = re.findall(link_pattern, line)
    if links:
        for link in links:
            domains.add(link)
lst = list()
for link in domains:
    lst.append(link)
lst.sort()
for el in lst:
    print(el)
# http://pastebin.com/raw/7543p0ns
