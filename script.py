import re

text = input('Введите текст:\n')
pattern = r'\D+'
matches = re.findall(pattern, text)
print(matches)