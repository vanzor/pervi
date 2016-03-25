# coding: utf-8
# первая строчка необходима для корректной работы с русскими символами
import requests
import urllib
import random
import os
import shutil
from bs4 import BeautifulSoup

# Получаем html код страницы
html = requests.get('http://kivano.kg').text

# Делаем этот код воспринимаемым для питона (для библиотеки BeautifulSoup, которую мы импортировали в 4 строке)
soup = BeautifulSoup(html, 'html.parser')

# Удаляем папку images если она уже существует и создаём новую
try:
	shutil.rmtree('images')
except:
	pass
	
os.makedirs('images')

# Создаём файл, который будет содержать ссылки на картинки
with open('output.txt', 'w') as f:
	# Выводим необходимые данные
	for x in soup.find_all('div', attrs={'class': 'product_img'}):
		url = x.find('a').find('img').get('src')
		if url[:4] == 'http':
			f.write(url + '\n')
			# Скачиваем картинку
			urllib.URLopener().retrieve(url, 'images/' + str(random.randint(1, 100)) + ".jpg")


