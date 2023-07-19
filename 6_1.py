import requests
from bs4 import BeautifulSoup


def get_top_songs(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Ошибка при запросе к серверу")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        songs = soup.find_all('div', class_='d-track__name')[
                :10]  # Песни на Яндекс. Музыке содержатся в блоках <div> с классом 'd-track__name'
    except AttributeError:
        print("Ошибка при поиске песен")
        return

    top_songs = []
    for song in songs:
        try:
            song_title = song.get_text(strip=True)  # Название песни содержится в тексте блока
            top_songs.append(song_title)
        except AttributeError:
            print("Ошибка при извлечении названия песни")

    return top_songs


# Пример использования
artist_url = input("Введите ссылку на исполнителя на Яндекс. Музыке: ")
top_songs = get_top_songs(artist_url)
if top_songs:
    print("Топ 10 песен:")
    for song in top_songs:
        print(song)
