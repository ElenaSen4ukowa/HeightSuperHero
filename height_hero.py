import requests

def get_height_hero(gender, has_job):
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    if response.status_code != 200:
        raise Exception('Failed to fetch data from API')

    heroes = response.json()
    filtered_heroes = []

    for hero in heroes:
        if hero['gender'] == gender and (has_job == (hero['work']['occupation'] != '')):
            filtered_heroes.append(hero)

    if not filtered_heroes:
        return None

    tallest_hero = max(filtered_heroes, key=lambda h: h['height'])
    return tallest_hero