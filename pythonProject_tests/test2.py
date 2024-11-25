import requests
import re

dict_alphabet = dict()
dict_keys = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
for i in dict_keys:
    dict_alphabet[i] = 0
for a in dict_keys:
    x = requests.get(
        f'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from=%3Cb%3E{a}%3C%2Fb%3E').text
    shab = r'<li><a href="/wiki/.*?'
    y = len(re.findall(shab, x)) - 4
    dict_alphabet[a] = y
with open('beasts.csv', 'a', encoding='utf-8') as f:
    f.write(str(dict_alphabet))
