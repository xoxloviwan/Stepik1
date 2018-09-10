import sys
import re

templ = r'(cat).*\1'
for line in sys.stdin:
    line = line.rstrip()
    if re.findall(templ, line):
        print(line)

# '.' - любой символ
# 'a*' - любое количество символа 'a', в том числе и 0
# '(cat)'  - поиск группы символов
# '(cat)\1' - повтор первой группы символов
