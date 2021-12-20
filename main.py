import requests

if __name__ == '__main__':

    token = '2619421814940190'
    url = 'https://superheroapi.com/api/'
    param = '/search/'
    names = ['Hulk', 'Captain America', 'Thanos']

    int_max = 0
    for name in names:
        response = requests.get(f'{url}{token}{param}{name}', timeout=5)
        dic = response.json()
        intelect = int(dic['results'][0]['powerstats']['intelligence'])
        if intelect > int_max:
            int_max = intelect
            int_name = name
    print(f'Самый умный супергерой: {int_name}')