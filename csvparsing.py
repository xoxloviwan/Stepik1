import requests
import csv
import collections

link = 'https://stepik.org/media/attachments/lesson/24473/Crimes.csv'
res = requests.get(link)
reader = csv.DictReader(res.text.splitlines())
cnt = collections.Counter()
for dct in reader:
    if '2015' in dct.get('Date'):
        cnt[dct.get('Primary Type')] += 1
print(cnt.most_common(1))
