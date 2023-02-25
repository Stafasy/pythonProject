import requests
import time

url = 'https://cloud-api.yandex.net/v1/disk/resources'
with open('requiremеnts.txt', 'r') as file:
    for line in file:
        token = line.strip()

headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}


class yandex:
    def __init__(self, token, url, headers):
        self.token = token
        self.url = url
        self.headers = headers

    def create_folder(self, path):
        """Создание папки. \n path: Путь к создаваемой папке."""
        requests.put(f'{url}?path={path}', headers=headers)

    def upload_file(self, url_load, params_load):
        p = requests.post(url=url_load, params=params_load, headers=headers)
        return p.json()


disk_load = yandex(token, url, headers)
disk_load.create_folder('foto')


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': user_id, 'fields': 'education,sex'}
        params.update(self.params)
        response = requests.get(url, params=params)
        return response.json()

    def users_photo(self):
        url = 'https://api.vk.com/method/photos.getAll'
        params = {'user_ids': user_id, 'album_id': 'saved', 'extended': 1, 'photo_sizes': 1}
        params.update(self.params)
        response = requests.get(url, params=params)
        return response.json()


with open('requiremеnts2.txt', 'r') as file:
    for line in file:
        access_token = line.strip()
user_id = '708255986'
vk = VK(access_token, user_id)
owner_id = -708255986
album_id = 'profile'

a = vk.users_photo()
x = 0
load_list = []
for s in a['response']['items']:
    for d in s['sizes'][x]['type']:
        if d != 'z':
            x += 1
        else:
            load_list.append(s['sizes'][x]['url'])

for v in load_list:
    url_load = ('https://cloud-api.yandex.net/v1/disk/resources/upload')
    params_load = {'path': '/foto/1.jpg', 'url': v}
    time.sleep(1)
    print(disk_load.upload_file(url_load, params_load))