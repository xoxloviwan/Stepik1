import requests
import csv

link = 'https://stepik.org/media/attachments/lesson/24473/Crimes.csv'
res = requests.get(link)
reader = csv.DictReader(res.text.splitlines())
for i in range(5):
    print(next(reader))
