import requests as rq
base_url = 'https://akabab.github.io/superhero-api/api'
name_list = ['Hulk', 'Captain America', 'Thanos']

def get_heroes_data(name_list):
    hero_stats = {}
    best_int = {}
    h_url = 'https://akabab.github.io/superhero-api/api/all.json'
    data = rq.get(h_url).json()
    for hero in name_list:
        for el in data:
            if el['name'] == hero:
                hero_stats[hero] = el['powerstats']['intelligence']
    max_int = max(hero_stats.values())
    best_int = {k: v for k, v in hero_stats.items() if v == max_int}
    result = f'Самый умный персонаж {list(best_int.keys())[0]}, его интеллект - {list(best_int.values())[0]}!'
    return result

if __name__ == '__main__':
    print(get_heroes_data(name_list))    