import os
import json
import requests

url = 'https://api.github.com/users/GefMar'
url2 = 'https://geekbrains.ru/'
img_url = 'https://d2xzmw6cctk25h.cloudfront.net/geekbrains/public/ckeditor_assets/pictures/9079/retina-aafea4920b176a7b7d965c6771e3795a.png'

# this_path = os.path.dirname(__file__)
# img_path = os.path.join(this_path, 'images', 'file_img.png')
# response = requests.get(img_url)
# data = response.content

# file = open('test.txt', 'w', encoding='UTF-8')
# file.write(data)
# file.close()

test_data = {
    'one': [1, 2, 3, 4],
    'two': (5.3, 4, 3, 2, 1),
    'thee': True,
    'four': None,
    'five': {
        'one': 'hello',
        'two': 'ПРИВЕТ МИР!12'
    },
}

with open('data.json', 'w') as file:
    file.write(json.dumps(test_data, ensure_ascii=False))

with open('data.json', 'r', encoding='UTF-8') as file:
    print(1)
    j_data = json.load(file)
    print(1)

# data = response.json()
print(1)
